from flask import Flask
from config import config
from . import api


database = {}  # multi dimentional dict storing application data in form of objects


def create_app(config_name):
    """
    Usage: Factory function used to setup the application instance
    :return: application instance
    """
    app = Flask(__name__)
    app.database = database
    app.config.from_object(config[config_name])

    app.register_blueprint(api.v1, url_prefix="/v1")
    return app
