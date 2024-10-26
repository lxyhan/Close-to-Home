import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGODB_URI = os.getenv('MONGODB_URI')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'disaster_relief_db')


# app/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from entity.user import MongoDB

# Initialize extensions
jwt = JWTManager()
socketio = SocketIO()

# Create MongoDB instance
mongo = MongoDB(Config.MONGODB_URI, Config.DATABASE_NAME)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    CORS(app)
    jwt.init_app(app)
    socketio.init_app(app)

    # Register blueprints
    from ..app.routes import auth, posts, donations, announcements, ml_analysis
    app.register_blueprint(auth.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(donations.bp)
    app.register_blueprint(announcements.bp)
    app.register_blueprint(ml_analysis.bp)

    return app
