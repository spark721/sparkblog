from flask_restful import fields
from ..extensions import db, bcrypt
from datetime import datetime


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
}


class User(db.Model):
    """Model for user accounts."""
    __tablename__ = 'users'

    # define columns
    id = db.Column(db.Integer,
                    primary_key=True)
    username = db.Column(db.String(),
                        unique=True,
                        nullable=False,
                        index=True)
    email = db.Column(db.String(),
                        unique=True,
                        nullable=False,
                        index=True)
    password = db.Column(db.String(),
                        nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    created = db.Column(db.DateTime,
                        default=datetime.utcnow,
                        nullable=False)

    def __init__(self, username, email, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def __repr__(self):
        return f'<User {self.username}>'
