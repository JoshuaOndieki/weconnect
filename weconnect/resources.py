from flask_restful import Resource


class UserRegistration(Resource):
    def post(self):
        """
            Returns:
                Success: {'message': 'Registration successful!'}
                Fail:    {'message': 'User exists!'}
        """
        return {'message': 'User registration'}


class UserLogin(Resource):
    def post(self):
        """
            Returns:
                Success: {'message': 'Login successful!'}
                Fail/existence:    {'message': 'User does not exist!'}
                Fail/credentials: {'message': 'Wrong username or password!'}
        """
        return {'message': 'User login'}


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
