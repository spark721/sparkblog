from flask import Blueprint, request
from flask_restful import Resource, Api, marshal_with
from ..models.user import User, user_fields, db


user_api_bp = Blueprint('user_api_bp', __name__)
user_api = Api(user_api_bp)


class UserAPI(Resource):
    
    def get(self):
        """Get a single user information."""
        return 'UserAPI GET method'

    @marshal_with(user_fields)
    def post(self):
        """Sign up a new user."""
        new_user = User(
            request.json['username'],
            request.json['email'],
            request.json['password'],
        )
        db.session.add(new_user)
        db.session.commit()

        return new_user

    def delete(self):
        """Delete a user account."""
        return 'UserAPI DELETE method'


user_api.add_resource(UserAPI, '/api/users')
