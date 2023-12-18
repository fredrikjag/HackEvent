from functools import wraps
from flask import request, jsonify


def validate_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.content_type != 'application/json':
            return jsonify({'error': 'Invalid Content-Type'}), 400
        try:
            request.get_json()
        except:
            return jsonify({'error': 'Invalid JSON data'}), 400
        return func(*args, **kwargs)
    return wrapper



if __name__ == "__main__":
    None