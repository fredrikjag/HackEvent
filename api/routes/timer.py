from tools import wrappers, formats
from flask import Blueprint, Response, jsonify, request
import time


timer_bp = Blueprint('timer', __name__)


duration_seconds: int = 7200
## Keeps track of the exakt time the event will end based in that the event has been stareted.
## So if the event duration is set to 10 seconds from now and the time right now is 16:00:00 then the variable would be set to 16:00:10
timer_end_time: int  = 0
time_left_seconds: int = 0
elapsed_seconds: int = 0
event_started: bool = False


def live_timer_sse():
    global duration_seconds
    global timer_end_time
    global time_left_seconds
    global elapsed_seconds
    global event_started
    

    while True:
        if timer_end_time == 0:
            time_left_formated = formats.format_time_left(duration_seconds)
            yield f'data:{time_left_formated}\n\n'

            time.sleep(1)
            continue

        if event_started:
            current_time = time.time()
            time_left = int(timer_end_time - current_time)

            ## Stops the timer from exceeding 00:00:00 and enables the timer to be reseted without killing the SSE Session.
            ## Thus allowing the timer to be reseted live for everyone without having to refresh the page.
            if time_left == 0:
                duration_seconds = 0
                timer_end_time = 0
                event_started = False

            time_left_formated = formats.format_time_left(time_left)
            yield f'data:{time_left_formated}\n\n'

            time_left_seconds = time_left
            elapsed_seconds = duration_seconds - time_left_seconds
            time.sleep(0.2)

            continue


@timer_bp.route('/event/timer', methods=['GET'])
def get_timer():
    return Response(live_timer_sse(), content_type='text/event-stream')   


@timer_bp.route('/event/duration', methods=['POST'])
@wrappers.validate_json
def set_event_duration():
    global duration_seconds

    data = request.get_json()
    
    if 'duration' in data:
        if type(data['duration']) != int:
            return jsonify({"message": "Provide integer value in seconds"}), 400

        duration_seconds = data['duration']
        return jsonify({"message": "Duration set"}), 200

    return jsonify({"message": "Missing duration key"}), 400


@timer_bp.route('/event/status', methods=['POST'])
@wrappers.validate_json
def set_event_status():
    global timer_end_time
    global duration_seconds
    global event_started

    data = request.get_json()

    if 'status' in data:
        status = data['status']
        
        if status is True:
            if duration_seconds <= 0:
                return jsonify({"message": "Set event duration first"}), 400
            timer_end_time = time.time() + duration_seconds
            event_started = True
            return jsonify({"message": "Event started"}), 200
        
        elif status is False:
            duration_seconds = int(timer_end_time - time.time())
            timer_end_time = 0
            event_started = False
            return jsonify({"message": "Event stopped"}), 200
        
        else:
            return jsonify({"message": "Provide boolean value"}), 400

    return jsonify({"message": "Missing status key"}), 400