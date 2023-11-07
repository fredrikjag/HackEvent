from flask import Blueprint, send_from_directory

common_bp = Blueprint('common', __name__)


@common_bp.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory("images/", filename)
    except Exception:
        return "Image not be found", 400