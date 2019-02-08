from flask import Flask
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    from app.api.V1 import party_view
    app.register_blueprint(party_view.B)
    return app
