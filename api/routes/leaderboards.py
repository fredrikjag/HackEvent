from flask import Blueprint

leaderboards_bp = Blueprint('leaderboards', __name__)



leaderboards_bp.route('/leaderboards')
def leaderboards():
    return