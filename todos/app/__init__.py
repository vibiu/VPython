from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.httpauth import HTTPBasicAuth

db = SQLAlchemy()
auth = HTTPBasicAuth()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .api_1_0 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/1.0')

    return app
