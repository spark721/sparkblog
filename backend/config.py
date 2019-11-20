import os


class Config():
    """Set Flask configuration vars."""

    # general config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    