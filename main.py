from functools import wraps
from flask import Flask, Response, request, jsonify, send_from_directory
from flask_cors import CORS
import time
import json


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


duration = 5
timer_end_time = 0
previous_seconds = None
event_started: bool = False

computers = None
leaderboards = None

#### Helpers


# def compare_flag(post_flag) -> bool | str:
#     for key, value in computers.items():
#         for computer in value:
#             for identity, flag in computer.items():
#                 if post_flag == flag:
#                     return True, key, identity
#     return False

# def find_leaderboard(computer):
#     for leaderboard in leaderboards:
#         if computer in leaderboard:
#             return leaderboard
#     return None

# def find_contestant_entry(leaderboard, contestant):
#     for entry in leaderboard:
#         if entry.get("contestant_name") == contestant:
#             return entry
#     return None


# def add_user_to_leaderboard(contestant, computer, identity):
#     leaderboard = find_leaderboard(computer)
    
#     if leaderboard is None:
#         return

#     contestant_entry = find_contestant_entry(leaderboard[computer], contestant)

#     if contestant_entry is not None:
#         if identity == "user" and "user_time" not in contestant_entry:
#             contestant_entry["user_time"] = get_time_left()
#             print(f"Updated user_time for {contestant} in {computer} leaderboard.")
#         elif identity == "root" and "root_time" not in contestant_entry:
#             contestant_entry["root_time"] = get_time_left() 
#         else:
#             return "Flag already registered"

#     new_entry = {"contestant_name": contestant}
#     if identity == "user":
#         new_entry["user_time"] = get_time_left()
#     elif identity == "root":
#         new_entry["root_time"] = get_time_left()

#     leaderboard[computer].append(new_entry)

#     return







def format_time_left(time_left: int):
    seconds = time_left % 60
    minutes = time_left // 60 % 60
    hours = time_left // 3600

    return f"{hours:02}:{minutes:02}:{seconds:02}"


# def get_time_left():
#     if timer_end_time != 0:
#         current_time = time.time()
#         time_left = timer_end_time - current_time
#         elapsed_time = int(time_left)

#         time_left = format_time_left(elapsed_time)

#         return time_left




#### WRAPPER's

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


#### SSE's

def live_timer_sse():
    global previous_seconds
    global event_started
    global duration
    global timer_end_time

    while True:
        if timer_end_time == 0:
            time_left_formated = format_time_left(duration)
            yield f'data:{time_left_formated}\n\n'

            time.sleep(1)
            continue

        if event_started:
            current_time = time.time()
            time_left = int(timer_end_time - current_time)

            ## Stops the timer from exceeding 00:00:00 and enables the timer to be reseted without killing the SSE Session.
            ## Thus allowing the timer to be reseted live for everyone without having to refresh the page.
            if time_left == 0:
                duration = 0
                timer_end_time = 0
                event_started = False

            time_left_formated = format_time_left(time_left)

            yield f'data:{time_left_formated}\n\n'
            previous_seconds = time_left
            time.sleep(0.2)
            continue


#### Routes

# @app.route('/api/leaderboard', methods=['GET'])
# def get_leaderboard():
#     return jsonify(leaderboards)


@app.route('/api/event/timer', methods=['GET'])
def get_timer():
    return Response(live_timer_sse(), content_type='text/event-stream')
    

@app.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory("images/", filename)
    except Exception:
        return "Image not be found", 400


# @app.route('/api/flag', methods=['POST'])
# @validate_json
# def post_flag():
#     data = request.get_json()

#     contestant = data['user']
#     flag = data['flag']

#     is_matched, computer, identity = compare_flag(flag)

#     if is_matched:
#         add_user_to_leaderboard(contestant, computer, identity)
#         return jsonify({"message": "Congrats"}), 200
    
#     return jsonify({"message": "Ouch, incorrect flag"}), 200


@app.route('/api/event/duration', methods=['POST'])
@validate_json
def set_event_duration():
    global duration

    data = request.get_json()

    if 'duration' in data:
        duration = data['duration']
        return jsonify({"message": "Duration set"}), 200

    return jsonify({"message": "Missing duration key"}), 400


@app.route('/api/event/status', methods=['POST'])
@validate_json
def set_event_status():
    global timer_end_time
    global duration
    global event_started

    data = request.get_json()

    if 'status' in data:
        status = data['status']
        
        if status is True:
            if duration <= 0:
                return jsonify({"message": "Set event duration first"}), 400
            timer_end_time = time.time() + duration
            event_started = True
            return jsonify({"message": "Event started"}), 200
        
        elif status is False:
            duration = timer_end_time - time.time()
            timer_end_time = None
            event_started = False
            return jsonify({"message": "Event stopped"}), 200
        
        else:
            return jsonify({"message": "Provide boolean value"}), 400

    return jsonify({"message": "Missing status key"}), 400



if __name__ == '__main__':
    # load_computers()
    # load_leaderboard()
    app.run(port=5000, debug=True, threaded=True)