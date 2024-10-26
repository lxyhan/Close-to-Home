# app/routes/posts.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.server.app import mongo
from ..entity.user import User, Post
from datetime import datetime

bp = Blueprint('posts', __name__)


@bp.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    user_id = get_jwt_identity()

    try:
        user = User.get_by_id(mongo, user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        if user.user_type == 'charity':
            success = user.create_post(
                text=data['text'],
                image=data.get('image'),
                event_details=data.get('event_details')
            )
        else:
            success = Post.create_help_post(
                db=mongo,
                user_id=user._id,
                text=data['text'],
                damage_description=data.get('damage_description'),
                image=data.get('image')
            )

        if success:
            return jsonify({'message': 'Post created successfully'}), 201
        return jsonify({'message': 'Failed to create post'}), 400

    except Exception as e:
        return jsonify({'message': 'Error creating post', 'error': str(e)}), 500


@bp.route('/posts', methods=['GET'])
def get_posts():
    try:
        post_type = request.args.get('type')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        skip = (page - 1) * per_page
        posts = Post.get_recent_posts(
            db=mongo,
            post_type=post_type,
            limit=per_page,
            skip=skip
        )

        # Enhance posts with user information
        enhanced_posts = []
        for post in posts:
            user = User.get_by_id(mongo, str(post['user_id']))
            post_data = {
                **post,
                'user_info': {
                    'id': str(user.id),
                    'name': user.name if hasattr(user, 'name') else f"{user.first_name} {user.last_name}",
                    'user_type': user.user_type
                }
            }
            enhanced_posts.append(post_data)

        return jsonify({
            'posts': enhanced_posts,
            'page': page,
            'per_page': per_page
        }), 200

    except Exception as e:
        return jsonify({'message': 'Error fetching posts', 'error': str(e)}), 500
