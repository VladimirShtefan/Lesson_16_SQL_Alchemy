import os

from flask import Flask

from app.blueprints.views import orders_blueprint
from app.configs.configs import DevConfig, ProdConfig
from data_base.creat_db import db

app = Flask(__name__)

app.register_blueprint(orders_blueprint)


if os.getenv('FLASK_ENV') == 'development':
    app.config.from_object(DevConfig)
else:
    app.config.from_object(ProdConfig)

db.init_app(app)
