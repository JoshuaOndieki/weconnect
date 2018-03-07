from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from weconnect.user_controller import UserController
from weconnect.business_controller import BusinessController
from weconnect.review_controller import ReviewController


user = UserController()
business = BusinessController()
review = ReviewController()

# jwt = app.jwt

# A storage engine to save revoked tokens. In production if
# speed is the primary concern, redis is a good bet. If data
# persistence is more important for you, postgres is another
# great option. In this example, we will be using an in memory
# store, just to show you how this might work. For more
# complete examples, check out these:
# https://github.com/vimalloc/flask-jwt-extended/blob/master/examples/redis_blacklist.py
# https://github.com/vimalloc/flask-jwt-extended/tree/master/examples/database_blacklist
# blacklist = set()
#
#
# # For this example, we are just checking if the tokens jti
# # (unique identifier) is in the blacklist set. This could
# # be made more complex, for example storing all tokens
# # into the blacklist with a revoked status when created,
# # and returning the revoked status in this call. This
# # would allow you to have a list of all created tokens,
# # and to consider tokens that aren't in the blacklist
# # (aka tokens you didn't create) as revoked. These are
# # just two options, and this can be tailored to whatever
# # your application needs.
# @app.jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#     jti = decrypted_token['jti']
#     return jti in blacklist


# Standard refresh endpoint. A blacklisted refresh token
# will not be able to access this endpoint
# @app.route('/refresh', methods=['POST'])
# @jwt_refresh_token_required
# def refresh():
#     current_user = get_jwt_identity()
#     ret = {
#         'access_token': create_access_token(identity=current_user)
#     }
#     return jsonify(ret), 200
#
#
# # Endpoint for revoking the current users access token
# @app.route('/logout', methods=['DELETE'])
# @jwt_required
# def logout():
#     jti = get_raw_jwt()['jti']
#     blacklist.add(jti)
#     return jsonify({"msg": "Successfully logged out"}), 200
#
#
# # Endpoint for revoking the current users refresh token
# @app.route('/logout2', methods=['DELETE'])
# @jwt_refresh_token_required
# def logout2():
#     jti = get_raw_jwt()['jti']
#     blacklist.add(jti)
#     return jsonify({"msg": "Successfully logged out"}), 200


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
        blacklist.add(jti)
        # self.response = user.logout(token)
        if self.response:
            return {'message': self.response[1]}


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
