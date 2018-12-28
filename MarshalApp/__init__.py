from flask import Flask

from MarshalApp.api import init_api
from MarshalApp.models import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123456@localhost:3306/my?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    init_api(app)
    return app