import json
from flask import Flask, request, jsonify, send_from_directory
import time

app = Flask(__name__)


####
#
#  Routes
#
####


# Define your /api/leaderboard route
@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify()

# Define your /api/flag route for POST requests
@app.route('/api/flag', methods=['POST'])
def post_flag():
    if request.headers.get('Content-Type') != 'application/json':
        return jsonify({'error': 'Invalid Content-Type'}), 400
    
    try:
        data = request.get_json()
    except Exception as e:
        print(f"Execption: {e}")
        return jsonify({'error': 'Invalid JSON data'}), 400
    
    if compare_flag(data['flag']):
        return jsonify({"message": "Congrats"}), 200
    
    return jsonify({"message": "Ouch, incorrect flag"}), 200

@app.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory("images/", filename)
    except Exception as e:
        print(e)
        return "Image not be found", 400



####
#
#  Helper Functions
#
####

def start_event():
    return

def set_event_duration():
    return

def load_computers() -> dict:
    computers = json.load(open("./computers.json"))
    return computers

def compare_flag(post_flag) -> bool | str:
    for k, v in computers.items():
        for c in v:
            for kk, vv in c.items():
                if post_flag == vv:
                    print(k)
                    return True, k

    return False

def add_user_to_leadboard(user, current_time):
    return


if __name__ == '__main__':
    computers = load_computers()
    app.run(port="", debug=True)
    
