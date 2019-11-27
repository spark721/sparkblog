from flask_restful import fields
from api import db, bcrypt
from datetime import datetime


post_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
}


class Post(db.Model):
    """Model for posts."""
    __tablename__ = 'posts'

    # define columns
    id = db.Column(db.Integer,
                    primary_key=True)
    title = db.Column(db.String(),
                        unique=True,
                        nullable=False)
    body = db.Column(db.String(),
                        nullable=False)
    author_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)
    created = db.Column(db.DateTime,
                        default=datetime.utcnow,
                        nullable=False)

    def __init__(self, title, body, **kwargs):
        super(Post, self).__init__(**kwargs)
        self.title = title
        self.body = body

    def __repr__(self):
        return f'<Post {self.title}>'
