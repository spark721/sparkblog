from flask_restful import fields
from ..extensions import db, bcrypt
from datetime import datetime


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
}


class User(db.Model):
    __tablename__ = 'users'

    # define columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.username = username
        self.password = bcrypt.generate_password_hash(password).encode('UTF-8')

    def __repr__(self):
        return f'<User {self.username}>'
