import os


class Config():
    """Set Flask configuration vars."""

    # general config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # authentication
    JWT_AUTH_URL_RULE = '/api/auth'

    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
