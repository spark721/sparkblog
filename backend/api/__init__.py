from flask import Flask


def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():

        return app
