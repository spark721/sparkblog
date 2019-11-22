from flask import Flask
from .extensions import db, bcrypt, migrate, jwt
from .resources.user import user_api_bp
from .auth import authenticate, identity


def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.authentication_handler(authenticate)
    jwt.identity_handler(identity)
    jwt.init_app(app)

    with app.app_context():
        # register blueprints
        app.register_blueprint(user_api_bp)

        return app
