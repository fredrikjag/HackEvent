from sqlalchemy import UUID
from data.db import db
import uuid
import json


class ServerClass(db.Model):
    __tablename__ = 'servers'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    server_name =  db.Column(db.String, nullable=False)
    server_user_flag = db.Column(db.String)
    server_root_flag = db.Column(db.String)
    server_ip = db.Column(db.String)
    server_image_link = db.Column(db.String)
  

    def __init__(self, id, server_name, server_user_flag, server_root_flag, server_ip, server_image_link):
        self.id = id
        self.server_name = server_name
        self.server_user_flag = server_user_flag
        self.server_root_flag = server_root_flag
        self.server_ip = server_ip
        self.server_image_link = server_image_link


    def __repr__(self):
        server_dict = {
            "id": str(self.id),
            "server_name": self.server_name,
            "server_user_flag": self.server_user_flag,
            "server_root_flag": self.server_root_flag, 
            "server_ip" : self.server_ip,
            "server_image_link": self.server_image_link
        }
        return json.dumps(server_dict)