from flask import Blueprint
from models.server import Server


servers_bp = Blueprint('servers', __name__)

@servers_bp.route("/servers")
def get_servers():

    server_data = Server.query.all()
    print(server_data)
    return "Hi", 200


