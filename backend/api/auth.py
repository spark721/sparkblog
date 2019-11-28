from .models.user import User
from .extensions import bcrypt


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if bcrypt.check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)
