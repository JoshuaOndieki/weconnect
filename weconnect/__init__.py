from flask import Flask
from config import config
from .api.v1.routes import v1


database = {"Users": None, "Businesses": None, "Reviews": None}  # multi dimentional dict storing app data in form of objects

"""
    ---------------------- DATA STRUCTURE -----------------
    {
        Users:
            {
                userx: [username, email, password]
                            ...
            }

        Businesses:
            {
                bsx: [bsid, name, location, category, userid]
                            ...
            }

        Reviews:
            {
                revx: [content, bsid, userid]
                            ...
            }
    }
"""

def create_app(config_name):
    """
    Usage: Factory function used to setup the application instance
    :return: application instance
    """
    app = Flask(__name__)
    app.database = database
    app.config.from_object(config[config_name])

    app.register_blueprint(v1, url_prefix="/api/v1")
    return app
