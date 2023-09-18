from functools import wraps
from flask import Flask, request, jsonify, send_from_directory
import time
import json


app = Flask(__name__)

class AppConfig:
    def __init__(self):
        self.event_duration = 0
        self.event_started = False


#### Helpers

def countdown_timer():
    if AppConfig.event_started: 
        for x in range(AppConfig.event_duration, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600) 
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)


def load_computers() -> dict:
    computers = json.load(open("./computers.json"))
    return computers

def compare_flag(post_flag) -> bool | str:
    for key, value in computers.items():
        for computer in value:
            for item, flag in computer.items():
                if post_flag == flag:
                    print(key)
                    return True, key
    return False


def add_user_to_leadboard(user, current_time):
    return


def validate_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.content_type != 'application/json':
            return jsonify({'error': 'Invalid Content-Type'}), 400
        try:
            request.get_json()
        except Exception as e:
            print(f"Exception: {e}")
            return jsonify({'error': 'Invalid JSON data'}), 400
        return func(*args, **kwargs)
    return wrapper


#### Routes

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify()

@app.route('/api/event/timer', methods=['GET'])
def get_timer():
    return jsonify()

@app.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory("images/", filename)
    except Exception as e:
        print(e)
        return "Image not be found", 400


@app.route('/api/flag', methods=['POST'])
@validate_json
def post_flag():
    data = request.get_json()
    if compare_flag(data['flag']):
        return jsonify({"message": "Congrats"}), 200
    
    return jsonify({"message": "Ouch, incorrect flag"}), 200

@app.route('/api/event/duration', methods=['POST'])
@validate_json
def set_event_duration():
    data = request.get_json()

    if 'duration' in data:
        AppConfig.event_duration = data['duration']
        return jsonify({"message": "Eventduration set"}), 200
    
    return jsonify({"message": "Missing duration key"}), 200


@app.route('/api/event/status', methods=['POST'])
@validate_json
def set_event_status():
    data = request.get_json()

    if 'status' in data:
        status = data['status']
        if status is True:
            AppConfig.event_started = True
            countdown_timer()
            return jsonify({"message": "Event started"}), 200
        elif status is False:
            return jsonify({"message": "Event stopped"}), 200
        else:
            return jsonify({"message": "Provide boolean value"}), 400

    return jsonify({"message": "Missing status key"}), 400



if __name__ == '__main__':
    computers = load_computers()
    app.run(port="", debug=True)





    
    
