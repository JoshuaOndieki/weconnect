from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from weconnect.user_controller import UserController
from weconnect.business_controller import BusinessController
from weconnect.review_controller import ReviewController


parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)
parser.add_argument('email')

user = UserController()
business = BusinessController()
review = ReviewController()


class UserRegistration(Resource):
    def post(self):
        """
            Returns:
                Success: {'message': 'Registration successful!'}
                Fail:    {'message': 'User exists!'}
        """
        data = parser.parse_args()
        response = user.create_user(data['username'], data['email'], data['password'])
        if response[0]:
            return {'message': 'Registration successful!'}, 201
        else:
            return {'message': 'User exists!'}


class UserLogin(Resource):
    def post(self):
        """
            Returns:
                Success: {'message': 'Login successful!'}
                Fail/existence:    {'message': 'User does not exist!'}
                Fail/credentials: {'message': 'Wrong username or password!'}
        """
        pass


class UserLogout(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserResetPassword(Resource):
    def post(self):
        return {'message': 'User Password reset'}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class Business(Resource):

    def get(self):
        return {'message': 'Retrieve all businesses'}

    def post(self):
        return {'message': 'Register Business'}


class BusinessHandler(Resource):
    def get(self, businessId):
        return {'message': 'Get specific business'}

    def put(self, businessId):
        return {'message': 'Update specific business'}

    def delete(self, businessId):
        return {'message': 'Delete a specific business'}


class Reviews(Resource):
    def get(self, businessId):
        return {'message': 'Retrieve reviews for a business'}

    def post(self, businessId):
        return {'message': 'Create review for a business'}
