from flask import Blueprint, request
from flask_restful import Resource, Api, marshal_with
from flask_jwt import jwt_required, current_identity
from ..models.post import Post, post_fields, db


post_api_bp = Blueprint('post_api_bp', __name__)
post_api = Api(post_api_bp)


class PostAPI(Resource):

    @marshal_with(post_fields)    
    def get(self):
        return Post.query.all()

    @marshal_with(post_fields)
    @jwt_required()
    def post(self):
        new_post = Post(
            request.json['title'],
            request.json['body'],
        )
        new_post.author_id = current_identity.id
        
        db.session.add(new_post)
        db.session.commit()
        return new_post


post_api.add_resource(PostAPI, '/api/post')
