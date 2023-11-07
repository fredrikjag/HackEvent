from tools import wrappers, formats
from flask import Blueprint, Response, jsonify, request
import time


timer_bp = Blueprint('timer', __name__)


duration: int = 5
timer_end_time:int  = 0
previous_seconds:int = 0
event_started: bool = False


def live_timer_sse():
    global previous_seconds
    global event_started
    global duration
    global timer_end_time

    while True:
        if timer_end_time == 0:
            time_left_formated = formats.format_time_left(duration)
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

            time_left_formated = formats.format_time_left(time_left)

            yield f'data:{time_left_formated}\n\n'
            previous_seconds = time_left
            time.sleep(0.2)
            continue


@timer_bp.route('/event/timer', methods=['GET'])
def get_timer():
    return Response(live_timer_sse(), content_type='text/event-stream')   


@timer_bp.route('/event/duration', methods=['POST'])
@wrappers.validate_json
def set_event_duration():
    global duration

    data = request.get_json()
    
    if 'duration' in data:
        if type(data['duration']) != int:
            return jsonify({"message": "Provide integer value in seconds"}), 400

        duration = data['duration']
        return jsonify({"message": "Duration set"}), 200

    return jsonify({"message": "Missing duration key"}), 400


@timer_bp.route('/event/status', methods=['POST'])
@wrappers.validate_json
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
            duration = int(timer_end_time - time.time())
            print(f"Seconds left: {duration}")
            timer_end_time = 0
            event_started = False
            return jsonify({"message": "Event stopped"}), 200
        
        else:
            return jsonify({"message": "Provide boolean value"}), 400

    return jsonify({"message": "Missing status key"}), 400