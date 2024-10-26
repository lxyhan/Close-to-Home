# app/routes/auth.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from src.server.app import mongo
from ..entity.user import BasicUser, Charity, User
from datetime import datetime, timedelta

bp = Blueprint('auth', __name__)


@bp.route('/register/user', methods=['POST'])
def register_user():
    data = request.get_json()

    try:
        # Convert string date to datetime object
        date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()

        user = BasicUser.create(
            db=mongo,
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=date_of_birth,
            city=data['city']
        )

        if user:
            access_token = create_access_token(identity=user.id)
            return jsonify({
                'message': 'User registered successfully',
                'access_token': access_token
            }), 201
        return jsonify({'message': 'Registration failed'}), 400

    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Registration failed', 'error': str(e)}), 500


@bp.route('/register/charity', methods=['POST'])
def register_charity():
    data = request.get_json()

    try:
        charity = Charity.create(
            db=mongo,
            email=data['email'],
            password=data['password'],
            name=data['name']
        )

        if charity:
            access_token = create_access_token(identity=charity.id)
            return jsonify({
                'message': 'Charity registered successfully',
                'access_token': access_token
            }), 201
        return jsonify({'message': 'Registration failed'}), 400

    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Registration failed', 'error': str(e)}), 500


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    try:
        user = User.get_by_email(mongo, data['email'])

        if not user or not check_password_hash(user.password, data['password']):
            return jsonify({'message': 'Invalid email or password'}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user_type': user.user_type
        }), 200

    except Exception as e:
        return jsonify({'message': 'Login failed', 'error': str(e)}), 500


@bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    try:
        user_id = get_jwt_identity()
        user = User.get_by_id(mongo, user_id)

        if not user:
            return jsonify({'message': 'User not found'}), 404

        # Return different profile data based on user type
        if isinstance(user, BasicUser):
            return jsonify({
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'city': user.city,
                'user_type': user.user_type
            })
        elif isinstance(user, Charity):
            return jsonify({
                'email': user.email,
                'name': user.name,
                'verified': user.verified,
                'user_type': user.user_type
            })

    except Exception as e:
        return jsonify({'message': 'Error fetching profile', 'error': str(e)}), 500
