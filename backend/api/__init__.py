from flask import Flask
from .extensions import db, bcrypt


def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        # initialize extensions
        db.init_app(app)
        bcrypt.init_app(app)
        

        return app
