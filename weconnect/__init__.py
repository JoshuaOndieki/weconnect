from flask import Flask
from config import config
from .api.v1.routes import v1
from flask_jwt_extended import JWTManager


# multi dimentional dict storing app data in form of objects
database = {"Users": {}, "Businesses": {}, "Reviews": {}}

"""
    ---------------------- DATA STRUCTURE -----------------
    {
        Users:
            {
                userx: [email, password]
                            ...
            }

        Businesses:
            {
                bsx: [name, location, category, userid]
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
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.jwt = JWTManager(app)
    app.blacklist = set()
    @app.jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in app.blacklist
    app.register_blueprint(v1, url_prefix="/api/v1")
    return app
