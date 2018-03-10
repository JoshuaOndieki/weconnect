from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token,
                                create_refresh_token, jwt_required,
                                get_jwt_identity, get_raw_jwt)
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
        self.parser.add_argument('username',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('password',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('email',
                                 help='This field cannot be blank',
                                 required=True)

    def post(self):
        """
            Returns:
                Success: {'message': 'Registration successful!'}
                Fail:    {'message': 'User exists!'}
        """
        data = self.parser.parse_args()
        self.response = user.create_user(data['username'],
                                         data['email'], data['password'])
        return {'message': self.response[1]}, 201


class UserLogin(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('password',
                                 help='This field cannot be blank',
                                 required=True)

    def post(self):
        """
            Usage: Login user and generate access token.
            Returns:
                Success: {'message': 'Login successful!'
                          'access_token': ''
                          'refresh_token': ''
                          }
                Fail/existence:    {'message': 'User does not exist!'}
                Fail/credentials: {'message': 'Wrong username or password!'}
        """
        data = self.parser.parse_args()
        self.current_user = user.find_by_username(data['username'])

        if not self.current_user:
            return {'message': 'No such user!'}, 404
        self.verified = user.login(data['username'], data['password'])
        if self.verified[0]:
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User login success!',
                'access_token': access_token,
                'refresh_token': refresh_token
                }, 200
        return {'message': self.verified[1]}, 401


class UserLogout(Resource):

    @jwt_required
    def post(self):
        """
            Revokes a token and blacklists it.
        """
        self.jti = get_raw_jwt()['jti']
        app.blacklist.add(self.jti)


class UserResetPassword(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('password',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('new_password',
                                 help='This field cannot be blank',
                                 required=True)

    @jwt_required
    def post(self):
        data = self.parser.parse_args()
        self.response = user.password_reset(data['username'],
                                            data['password'],
                                            data['new_password'])
        if self.response:
            return {'message': self.response[1]}


class Business(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('location',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('category',
                                 help='This field cannot be blank',
                                 required=True)

    def get(self):
        self.businesses = business.get_businesses()
        return self.businesses[1], 200

    @jwt_required
    def post(self):
        username = get_jwt_identity()
        data = self.parser.parse_args()
        self.response = business.create_business(data['name'],
                                                 data['location'],
                                                 data['category'],
                                                 username)
        return {'message': self.response[1]}


class BusinessHandler(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('location',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('category',
                                 help='This field cannot be blank',
                                 required=True)

    def get(self, businessId):
        self.response = business.get_business_by_id(businessId)
        return self.response[1], 200

    @jwt_required
    def put(self, businessId):
        data = self.parser.parse_args()
        user_id = get_jwt_identity()
        self.response = business.edit(businessId,
                                      data['name'],
                                      data['location'],
                                      data['category'],
                                      user_id)
        return {'message': self.response[1]}, 201

    @jwt_required
    def delete(self, businessId):
        username = get_jwt_identity()
        self.response = business.delete_business(businessId, username)
        if self.response:
            return {'message': self.response[1]}


class Reviews(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('content',
                                 help='This field cannot be blank',
                                 required=True)

    def get(self, businessId):
        self.response = review.retrieve_reviews(businessId)
        if self.response[0]:
            return {'message': self.response[1]}, 200
        return {'message': self.response[1]}, 404

    @jwt_required
    def post(self, businessId):
        data = self.parser.parse_args()
        content = data['content']
        user_id = get_jwt_identity()
        self.response = review.create_review(content, businessId, user_id)
        return {'message': self.response[1]}, 201


class All(Resource):
    def get(self):
        self.database = app.database
        return self.database, 200
