"""Module for user management usingMongoDB."""
from datetime import datetime
import pymongo
from pymongo import MongoClient
from bson import ObjectId
from typing import Optional, Dict, List
from werkzeug.security import generate_password_hash

class MongoDB:
    def __init__(self, connection_string: str, db_name: str):
        """Initialize MongoDB connection."""
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]

        # Create indexes
        self.db.users.create_index([("email", pymongo.ASCENDING)], unique=True)
        self.db.posts.create_index([("user_id", pymongo.ASCENDING)])

    def close(self):
        """Close MongoDB connection."""
        self.client.close()

class User():
    """Base user class for all types of users in system."""

    def __init__(self, db: MongoDB, **kwargs):
        self.db = db
        self._id = kwargs.get('_id')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.user_type = kwargs.get('user_type', 'user')

    @property
    def id(self):
        return str(self._id) if self._id else None

    @classmethod
    def get_by_id(cls, db: MongoDB, user_id: str) -> Optional['User']:
        """Get user by ID."""
        try:
            user_data = db.db.users.find_one({'id': ObjectId(user_id)})
            if not user_data:
                return None

            if user_data['user_type'] == 'basic_user':
                return BasicUser(db, **user_data)
            elif user_data['user_type'] == 'charity':
                return Charity(db, **user_data)
            return User(db, **user_data)
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    @classmethod
    def get_by_email(cls, db: MongoDB, email: str) -> Optional['User']:
        """Get user by email."""
        try:
            user_data = db.db.users.find_one({'email': email})
            if not user_data:
                return None

            if user_data['user_type'] == 'basic_user':
                return BasicUser(db, **user_data)
            elif user_data['user_type'] == 'charity':
                return Charity(db, **user_data)
            return User(db, **user_data)
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    def create_post(self, text: str, image: Optional[str] = None) -> bool:
        """Create a new post."""
        try:
            post_data = {
                'user_id': self._id,
                'text': text,
                'image': image,
                'created_at': datetime.utcnow()
            }
            result = self.db.db.posts.insert_one(post_data)
            return bool(result.inserted_id)
        except Exception as e:
            print(f"Error creating post: {e}")
            return False

    def get_posts(self, limit: int = 10, skip: int = 0) -> List[Dict]:
        """Get user's posts with pagination."""
        try:
            cursor = self.db.db.posts.find(
                {'user_id': self._id}
            ).sort('created_at', -1).skip(skip).limit(limit)
            return list(cursor)
        except Exception as e:
            print(f"Error fetching posts: {e}")
            return []

class BasicUser(User):
    """Regular user (i.e., a Person)."""

    def __init__(self, db: MongoDB, **kwargs):
        super().__init__(db, **kwargs)
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.date_of_birth = kwargs.get('date_of_birth')
        self.city = kwargs.get('city')
        self.user_type = 'basic_user'

    @classmethod
    def create(cls, db: MongoDB, email: str, password: str, first_name: str,
               last_name: str, date_of_birth: datetime, city: str) -> Optional['BasicUser']:
        """Create a new basic user."""
        try:
            if db.db.users.find_one({'email': email}):
                raise ValueError("Email already exists")

            user_data = {
                'email': email,
                'password': generate_password_hash(password),
                'user_type': 'basic_user',
                'first_name': first_name,
                'last_name': last_name,
                'date_of_birth': date_of_birth,
                'city': city,
                'created_at': datetime.utcnow()
            }

            result = db.db.users.insert_one(user_data)
            user_data['_id'] = result.inserted_id
            return cls(db, **user_data)
        except Exception as e:
            print(f"Error creating user: {e}")
            return None

class Charity(User):
    """Charity organization user."""

    def __init__(self, db: MongoDB, **kwargs):
        super().__init__(db, **kwargs)
        self.name = kwargs.get('name')
        self.verified = kwargs.get('verified', False)
        self.user_type = 'charity'

    @classmethod
    def create(cls, db: MongoDB, email: str, password: str, name: str,
               verified: bool = False) -> Optional['Charity']:
        """Create a new charity user."""
        try:
            if db.db.users.find_one({'email': email}):
                raise ValueError("Email already exists")

            user_data = {
                'email': email,
                'password': generate_password_hash(password),
                'user_type': 'charity',
                'name': name,
                'verified': verified,
                'created_at': datetime.now(datetime.timezone.utc)
            }

            result = db.db.users.insert_one(user_data)
            user_data['_id'] = result.inserted_id
            return cls(db, **user_data)
        except Exception as e:
            print(f"Error creating charity: {e}")
            return None

    def create_post(self, text: str, image: Optional[str] = None,
                    event_details: Optional[str] = None) -> bool:
        """Create a charity announcement post."""
        try:
            post_data = {
                'user_id': self._id,
                'text': f"Charity Announcement: {text}",
                'image': image,
                'event_details': event_details,
                'post_type': 'charity_post',
                'created_at': datetime.now(datetime.timezone.utc)
            }
            result = self.db.db.posts.insert_one(post_data)
            return bool(result.inserted_id)
        except Exception as e:
            print(f"Error creating charity post: {e}")
            return False

class Post:
    """Base post class with MongoDB integration."""

    @classmethod
    def create_help_post(cls, db: MongoDB, user_id: ObjectId, text: str,
                        damage_description: Optional[str] = None,
                        image: Optional[str] = None) -> bool:
        """Create a help post."""
        try:
            post_data = {
                'user_id': user_id,
                'text': text,
                'image': image,
                'damage_description': damage_description,
                'post_type': 'help_post',
                'created_at': datetime.utcnow()
            }
            result = db.db.posts.insert_one(post_data)
            return bool(result.inserted_id)
        except Exception as e:
            print(f"Error creating help post: {e}")
            return False

    @classmethod
    def get_recent_posts(cls, db: MongoDB, post_type: Optional[str] = None,
                        limit: int = 10, skip: int = 0) -> List[Dict]:
        """Get recent posts with optional filtering by type."""
        try:
            query = {'post_type': post_type} if post_type else {}
            cursor = db.db.posts.find(query).sort(
                'created_at', -1
            ).skip(skip).limit(limit)
            return list(cursor)
        except Exception as e:
            print(f"Error fetching posts: {e}")
            return []
