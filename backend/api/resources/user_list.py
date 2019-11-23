from flask import Blueprint
from flask_restful import Resource, Api, marshal_with
from ..models.user import User, user_fields, db


userlist_api_bp = Blueprint('userlist_api_bp', __name__)
userlist_api = Api(userlist_api_bp)


class UserListAPI(Resource):
    
    @marshal_with(user_fields)
    def get(self):
        return User.query.all()


userlist_api.add_resource(UserListAPI, '/api/users')
