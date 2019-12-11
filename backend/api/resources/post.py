from flask import Blueprint, request
from flask_restful import Resource, Api, marshal_with
from flask_jwt import jwt_required, current_identity
from ..models.post import Post, post_fields, db


post_api_bp = Blueprint('post_api_bp', __name__)
post_api = Api(post_api_bp)


class PostAPI(Resource):
    """API for single post actions."""
    @marshal_with(post_fields)
    def get(self, id):
        return Post.query.get(id)

    @marshal_with(post_fields)
    def delete(self, id):
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return post

post_api.add_resource(PostAPI, '/api/post/<int:id>')
