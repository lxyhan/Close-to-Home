from flask import Flask
from flask_cors import CORS
from config import Config
# app/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize extensions
jwt = JWTManager()
socketio = SocketIO()

# MongoDB connection
mongo_client = MongoClient(os.getenv('MONGODB_URI'))
db = mongo_client.disaster_relief_db


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['MONGO_URI'] = os.getenv('MONGODB_URI')

    # Initialize extensions
    CORS(app)
    jwt.init_app(app)
    socketio.init_app(app)

    # Register blueprints
    from app.routes import auth, posts, donations, announcements, ml_analysis
    app.register_blueprint(auth.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(donations.bp)
    app.register_blueprint(announcements.bp)
    app.register_blueprint(ml_analysis.bp)

    return app


# app/models.py
from datetime import datetime
from bson import ObjectId

# Schema definitions for MongoDB collections
user_schema = {
    "username": str,
    "email": str,
    "password_hash": str,
    "user_type": str,  # 'individual', 'charity', 'medical_unit'
    "created_at": datetime
}

post_schema = {
    "content": str,
    "location": str,
    "coordinates": {
        "latitude": float,
        "longitude": float
    },
    "severity": str,
    "user_id": ObjectId,
    "created_at": datetime
}

announcement_schema = {
    "title": str,
    "content": str,
    "location": str,
    "event_datetime": datetime,
    "charity_id": ObjectId,
    "created_at": datetime
}

donation_schema = {
    "amount": float,
    "item_description": str,
    "donor_id": ObjectId,
    "recipient_id": ObjectId,
    "status": str,  # 'pending', 'completed', 'cancelled'
    "created_at": datetime
}


# Create MongoDB indexes
def setup_indexes():
    db.users.create_index("email", unique=True)
    db.users.create_index("username", unique=True)
    db.posts.create_index([("coordinates", "2dsphere")])
    db.posts.create_index("created_at")
    db.announcements.create_index("event_datetime")
    db.donations.create_index("created_at")
