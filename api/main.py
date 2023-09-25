from functools import wraps
from flask import Flask, request, jsonify, send_from_directory
import time
import json


app = Flask(__name__)

timer_end_time = 0
duration = 0
computers = None
leaderboards = None

#### Helpers

def load_computers():
    global computers
    computers = json.load(open("./computers.json"))

def load_leaderboard():
    global leaderboards
    leaderboards = json.load(open("./leaderboards.json"))

def write_leaderboard():
    global leaderboards
    leaderboards = json.dumps(open("./leaderboards.json"), indent=4)

def compare_flag(post_flag) -> bool | str:
    for key, value in computers.items():
        for computer in value:
            for identity, flag in computer.items():
                if post_flag == flag:
                    return True, key, identity
    return False

def get_time_used():
    seconds = duration % 60
    minutes = int(duration / 60) % 60
    hours = int(duration / 3600) 
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def find_leaderboard(computer):
    for leaderboard in leaderboards:
        if computer in leaderboard:
            return leaderboard
    return None

def find_contestant_entry(leaderboard, contestant):
    for entry in leaderboard:
        if entry.get("contestant_name") == contestant:
            return entry
    return None

def add_user_to_leaderboard(contestant, computer, identity):
    leaderboard = find_leaderboard(computer)
    
    if leaderboard is None:
        return

    contestant_entry = find_contestant_entry(leaderboard[computer], contestant)

    if contestant_entry is not None:
        if identity == "user" and "user_time" not in contestant_entry:
            contestant_entry["user_time"] = get_time_used()
            print(f"Updated user_time for {contestant} in {computer} leaderboard.")
        elif identity == "root" and "root_time" not in contestant_entry:
            contestant_entry["root_time"] = get_time_used() 
        else:
            return "Flag already registered"

    new_entry = {"contestant_name": contestant}
    if identity == "user":
        new_entry["user_time"] = get_time_used()
    elif identity == "root":
        new_entry["root_time"] = get_time_used()

    leaderboard[computer].append(new_entry)

    print(leaderboards)

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
    global timer_end_time

    if timer_end_time is None:
        return jsonify({'time_left': duration}), 200

    current_time = time.time()
    time_left = timer_end_time - current_time

    if time_left <= 0:
        return jsonify({'time_left': 0}), 200

    return jsonify({'time_left': int(time_left)}), 200
    

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

    contestant = data['user']
    flag = data['flag']

    is_matched, computer, identity = compare_flag(flag)

    if is_matched:
        add_user_to_leaderboard(contestant, computer, identity)
        return jsonify({"message": "Congrats"}), 200
    
    return jsonify({"message": "Ouch, incorrect flag"}), 200

@app.route('/api/event/duration', methods=['POST'])
@validate_json
def set_event_duration():
    global duration

    data = request.get_json()

    if 'duration' in data:
        duration = data['duration']
        return jsonify({"message": "Duration set"}), 200

    return jsonify({"message": "Missing duration key"}), 200


@app.route('/api/event/status', methods=['POST'])
@validate_json
def set_event_status():
    global timer_end_time
    global duration

    data = request.get_json()

    if 'status' in data:
        status = data['status']
        if status is True:
            if duration <= 0:
                return jsonify({"message": "Set event duration first"}), 200
            timer_end_time = time.time() + duration
            return jsonify({"message": "Event started"}), 200
        elif status is False:
            duration = timer_end_time - time.time()
            timer_end_time = None
            return jsonify({"message": "Event stopped"}), 200
        else:
            return jsonify({"message": "Provide boolean value"}), 400

    return jsonify({"message": "Missing status key"}), 400



if __name__ == '__main__':
    load_computers()
    load_leaderboard()
    app.run(port=5000, debug=True)





    
    
