from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask import current_app as app

from weconnect.user_controller import UserController
from weconnect.business_controller import BusinessController
from weconnect.review_controller import ReviewController


user = UserController()
business = BusinessController()
review = ReviewController()


class UserRegistration(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', help='This field cannot be blank', required=True)
        self.parser.add_argument('password', help='This field cannot be blank', required=True)
        self.parser.add_argument('email', help='This field cannot be blank', required=True)

    def post(self):
        """
            Returns:
                Success: {'message': 'Registration successful!'}
                Fail:    {'message': 'User exists!'}
        """
        data = self.parser.parse_args()
        response = user.create_user(data['username'], data['email'], data['password'])
        if response[0]:
            return {'message': 'Registration successful!'}, 201
        else:
            return {'message': 'User exists!'}


class UserLogin(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', help='This field cannot be blank', required=True)
        self.parser.add_argument('password', help='This field cannot be blank', required=True)

    def post(self):
        """
            Usage: Login user and generate access token.
            Returns:
                Success: {'message': 'Login successful!'}
                Fail/existence:    {'message': 'User does not exist!'}
                Fail/credentials: {'message': 'Wrong username or password!'}
        """
        data = self.parser.parse_args()
        current_user = user.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User does not exist!'}, 404
        verified = user.login(data['username'], data['password'])
        if verified[0]:
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'Login successful!',
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        return {'message': 'Wrong username or password!'}, 401


class UserLogout(Resource):

    @jwt_required
    def post(self):
        """
            Revokes a token and blacklists it.
        """
        # token = get_raw_jwt()
        jti = get_raw_jwt()['jti']
        app.blacklist.add(jti)
        print(app.blacklist)
        # self.response = user.logout(token)
        # if self.response:
        #     return {'message': self.response[1]}


class UserResetPassword(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', help='This field cannot be blank', required=True)
        self.parser.add_argument('password', help='This field cannot be blank', required=True)
        self.parser.add_argument('new_password', help='This field cannot be blank', required=True)

    @jwt_required
    def post(self):
        data = self.parser.parse_args()
        current_user = get_jwt_identity()
        print('*******************************************')
        print(current_user)
        self.response = user.password_reset(data['username'], data['password'], data['new_password'])
        if self.response:
            return {'message': self.response[1]}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class Business(Resource):

    def get(self):
        self.businesses = business.retrieve_business()
        return self.businesses[1], 200

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
