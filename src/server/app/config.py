import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('FLASK_DEBUG', True)
    MONGO_URI = os.getenv('MONGO_URI')

    # Validate required environment variables
    @classmethod
    def validate_config(cls):
        if not cls.MONGO_URI:
            raise ValueError("MONGO_URI environment variable is not set")
        if not cls.SECRET_KEY:
            raise ValueError("SECRET_KEY environment variable is not set")
