from models.contestant import ContestantClass
from models.server import ServerClass
from data.db import db
from .formats import format_time_left
import routes.timer
import uuid


def verify_flag(contestant_name: str, flag: str) -> bool:
    servers_all = ServerClass.query.all()

    identity = None

    for s in servers_all:
        server_id = s.id
        if flag == s.server_user_flag:
            identity = "user"
        if flag == s.server_root_flag:
            identity = "root"
    
    if identity:
        print(server_id)
        add_user_to_leaderboard(contestant_name, server_id, identity)
        return True
        
    
    return False


def add_user_to_leaderboard(contestant_name, server_id, identity):
    
    new_contestant = ContestantClass(
        id = generate_uuid4(),
        contestant_name = contestant_name,
        server_id = server_id,
        contestant_user_time = "",
        contestant_root_time = ""
    )

    if identity == "user":
        new_contestant.contestant_user_time = format_time_left(routes.timer.elapsed_seconds)
    else:
        new_contestant.contestant_root_time = format_time_left(routes.timer.elapsed_seconds)

    db.session.add(new_contestant)
    db.session.commit()
    return

def generate_uuid4():
    return uuid.uuid4()

if __name__ == "__main__":
    None