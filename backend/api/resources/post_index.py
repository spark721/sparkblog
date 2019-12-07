from flask import Blueprint, request
from flask_restful import Resource, Api, marshal_with
from flask_jwt import jwt_required, current_identity
from ..models.post import Post, post_fields, db


postindex_api_bp = Blueprint('postindex_api_bp', __name__)
postindex_api = Api(postindex_api_bp)


class PostIndexAPI(Resource):

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


postindex_api.add_resource(PostIndexAPI, '/api/posts')
