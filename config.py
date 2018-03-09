import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Application configuration
    """
    SECRET_KEY = 'secret'
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    DEBUG = True


config = {'development': DevelopmentConfig, 'testing': TestingConfig, 'production': ProductionConfig}
