# Initialize your project
from flask import Flask
from flask_restful import Api

from .database import db
from .config import Config
from .models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)

    return app, api


app, api = create_app()