from sqlalchemy import UUID
from data.db import db
import uuid
import json


class Contestant(db.Model):
    __tablename__ = 'contestats'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contestant_name =  db.Column(db.String, nullable=False)
    contestant_user_time = db.Column(db.String)
    contestant_root_time = db.Column(db.String)
    server_id = db.Column(uuid, db.ForeignKey('server.id'))

    def __init__(self, id, contestant_name, contestant_user_time, contestant_root_time, server_id):
        self.id = id
        self.contestant_name = contestant_name
        self.contestant_user_time = contestant_user_time
        self.contestant_root_time = contestant_root_time
        self.server_id = server_id

    def __repr__(self):
        return f"<Contestant {self.contestant_name} {self.contestant_user_time} {self.contestant_root_time}>"