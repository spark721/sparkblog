from flask import Blueprint
from flask_restful import Resource, Api, marshal_with
from flask_jwt import jwt_required


post_api_bp = Blueprint('post_api_bp', __name__)
post_api = Api(post_api_bp)


class PostAPI(Resource):
    
    def get(self):
        return f'PostAPI GET method'


post_api.add_resource(PostAPI, '/api/post')
