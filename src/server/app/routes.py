from flask import Blueprint, jsonify, request, current_app
from bson import json_util
import json

# Change the name of the blueprint instance
def get_main_blueprint():
    return Blueprint('main', __name__)

# Define your collection name
main_blueprint = get_main_blueprint()
COLLECTION_NAME = 'your_collection_name'

@main_blueprint.route('/api/data', methods=['POST'])
def add_data():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        result = current_app.db[COLLECTION_NAME].insert_one(data)
        return jsonify({
            'message': 'Data added successfully',
            'id': str(result.inserted_id)
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main_blueprint.route('/api/data', methods=['GET'])
def get_data():
    try:
        data = current_app.db[COLLECTION_NAME].find()
        # Use json_util to properly handle MongoDB ObjectId
        return json.loads(json_util.dumps(list(data)))
    except Exception as e:
        return jsonify({'error': str(e)}), 500
