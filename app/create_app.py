from typing import Type

from flask import Flask

from app.configs.configs import Config
from data_base.create_db import db
from data_base.models.user_model import User


def create_app(config: Type[Config]) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    @app.before_first_request
    def test():
        db.create_all()

    @app.route('/')
    def main():
        return 'ok'

    return app
