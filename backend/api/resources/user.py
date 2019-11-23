from flask import Blueprint, request
from flask_restful import Resource, Api, marshal_with
from flask_jwt import jwt_required, current_identity
from ..models.user import User, user_fields, db


user_api_bp = Blueprint('user_api_bp', __name__)
user_api = Api(user_api_bp)


class UserAPI(Resource):
    
    @marshal_with(user_fields)
    @jwt_required()
    def get(self):
        """Get a single user information."""
        return current_identity

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


user_api.add_resource(UserAPI, '/api/user')
