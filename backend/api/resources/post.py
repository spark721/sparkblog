from flask import Blueprint, request
from flask_restful import Resource, Api, marshal_with
from flask_jwt import jwt_required, current_identity
from ..models.post import Post, post_fields, db


post_api_bp = Blueprint('post_api_bp', __name__)
post_api = Api(post_api_bp)


class PostAPI(Resource):
    @marshal_with(post_fields)
    def get(self, id):
        return Post.query.get(id)

post_api.add_resource(PostAPI, '/api/post/<int:id>')