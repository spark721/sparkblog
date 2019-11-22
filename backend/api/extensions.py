from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt import JWT


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
jwt = JWT()
