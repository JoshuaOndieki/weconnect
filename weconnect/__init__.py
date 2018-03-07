from flask import Flask
from config import config
from .api.v1.routes import v1
from flask_jwt_extended import JWTManager


database = {"log": {'token_blacklist': []}, "Users": {}, "Businesses": {}, "Reviews": {}}  # multi dimentional dict storing app data in form of objects

"""
    ---------------------- DATA STRUCTURE -----------------
    {
        log:
            {
                token_blacklist: []
            }

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
    blacklist = set()
    # # For this example, we are just checking if the tokens jti
    # # (unique identifier) is in the blacklist set. This could
    # # be made more complex, for example storing all tokens
    # # into the blacklist with a revoked status when created,
    # # and returning the revoked status in this call. This
    # # would allow you to have a list of all created tokens,
    # # and to consider tokens that aren't in the blacklist
    # # (aka tokens you didn't create) as revoked. These are
    # # just two options, and this can be tailored to whatever
    # # your application needs.
    #
    @app.jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist
    app.register_blueprint(v1, url_prefix="/api/v1")
    return app
