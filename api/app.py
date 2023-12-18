from flask import Flask
from routes import timer, leaderboards, admin, common, servers
from data.db import db
import models.server
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager
from flask_cors import CORS


env_user = "hackevent"
env_password = "hackeventpassword"
env_database = "ctf"
env_host = "localhost"
env_port = 5433

app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{env_user}:{env_password}@{env_host}:{env_port}/{env_database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "bc97cd2763bb929048bb514faeeed18f"
db.init_app(app)


# jwt = JWTManager()
# jwt.init_app(app)

app.register_blueprint(timer.timer_bp, url_prefix='/api/v1/t')
app.register_blueprint(leaderboards.leaderboards_bp, url_prefix='/api/v1/l')
app.register_blueprint(servers.servers_bp, url_prefix='/api/v1/s')
app.register_blueprint(admin.admin_bp, url_prefix='/api/v1/event_admin')
app.register_blueprint(common.common_bp, url_prefix='/common')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)