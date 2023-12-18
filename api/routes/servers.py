from flask import Blueprint, jsonify, request
from tools.helpers import verify_flag
from tools.wrappers import validate_json
from models.server import ServerClass


servers_bp = Blueprint('servers', __name__)

@servers_bp.route("/servers")
def get_servers_details():
    servers_all = ServerClass.query.all()
    
    server_details = []
    [server_details.append({"id": server.id, "name": server.server_name, "ip_addr": server.server_ip, "image_link": server.server_image_link}) for server in servers_all]
    
    return jsonify(server_details), 200


@servers_bp.route("/flag", methods=['POST'])
@validate_json
def post_flag():

    data = request.get_json()
        
    try: 
        contestant = data['contestant']
        flag = data['flag']
    except:
        return jsonify({"message": "Missing keys user or flag"}), 400

    is_matched = verify_flag(contestant, flag)

    if not is_matched:
        return jsonify({"message": "Ouch, incorrect flag"}), 200
    
    return jsonify({"message": "Congrats"}), 200
    
    