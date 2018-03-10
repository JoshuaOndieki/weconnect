import unittest
import json
from weconnect import create_app


class TestApiEndpoints(unittest.TestCase):
    """
        Tests User API endpoints
        - UserRegistration:     '/api/v1/auth/register'         # POST
        - UserLogin:            '/api/v1/auth/login'            # POST
        - UserLogout:           '/api/v1/auth/logout'           # POST
        - UserResetPassword:    '/api/v1/auth/reset-password'   # POST
        Tests Business API endpoints
        - Business:         '/api/v1/businesses'                # GET
        - Business:         '/api/v1/businesses'                # POST
        - BusinessHandler:  '/api/v1/businesses/<businessId>'   # GET
        - BusinessHandler:  '/api/v1/businesses/<businessId>'   # PUT
        - BusinessHandler:  '/api/v1/businesses/<businessId>'   # DEL
        Tests Review API endpoints
        - Reviews:   '/api/v1/businesses/<businessId>/reviews'  # GET
        - Reviews:   '/api/v1/businesses/<businessId>/reviews'  # POST
    """

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.headers = {'content-type': 'application/json'}
        self.context = self.app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_user_registration_successful_with_acceptable_info(self):
        data = {"username": "user1",
                "email": "user1@email.com",
                "password": "user1pass"}
        self.response = self.client().post('/api/v1/auth/register', data=data)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'], "User creation successful!")
        self.assertEqual(self.response.status_code, 201)

    def test_does_not_allow_duplicate_registration(self):
        data = {"username": "dupuser",
                "email": "dupuser@email.com",
                "password": "dupuserpass"}
        self.response = self.client().post('/api/v1/auth/register', data=data)
        self.assertEqual(self.response.status_code, 201)

        self.response = self.client().post('/api/v1/auth/register', data=data)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'], "Username exists!")
        self.assertEqual(self.response.status_code, 201)

    def test_user_login_successful_with_matching_user_info(self):
        data = {"username": "loginuser",
                "email": "loginuser@email.com",
                "password": "luserpass"}
        self.client().post('/api/v1/auth/register', data=data)
        self.response = self.client().post('/api/v1/auth/login', data=data)
        self.assertEqual(self.response.status_code, 200)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'], "User login success!")
        self.assertTrue(result['access_token'])

    def test_does_not_allow_non_user_login(self):
        data = {"username": "null", "password": "nullpass"}
        self.response = self.client().post('/api/v1/auth/login', data=data)
        self.assertEqual(self.response.status_code, 401)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'], "No such user!")

    def test_does_not_allow_login_with_wrong_info(self):
        data = {"username": "guessuser",
                "email": "guessuser@email.com",
                "password": "gpass"}
        self.client().post('/api/v1/auth/register', data=data)
        data = {"username": "guessuser", "password": "guessed"}
        self.response = self.client().post('/api/v1/auth/login', data=data)
        self.assertEqual(self.response.status_code, 401)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'], "Wrong password!")

    def test_get_all_businesses(self):
        self.response = self.client().get('/api/v1/businesses')
        self.assertTrue(self.response.status_code is 200)

    def test_create_business(self):
        data = {"username": "bsowner",
                "password": "bsopass",
                "email": "bsowner@email.com"}
        self.client().post('/api/v1/auth/register', data=data)
        self.response = self.client().post('/api/v1/auth/login', data=data)
        result = json.loads(self.response.data.decode())
        access_token = result['access_token']
        data = {'name': 'bs1', 'location': 'loc1', 'category': 'cat1'}
        self.response = self.client().post(
                        '/api/v1/businesses', data=data,
                        headers=dict(Authorization="Bearer " + access_token))
        self.assertTrue(self.response.status_code, 201)

    def test_retrieve_a_business(self):
        self.response = self.client().get('/api/v1/businesses/1')
        self.assertTrue(self.response.status_code is 200)

    def test_update_a_business(self):
        data = {"username": "bsuser", "password": "bsuserpass"}
        self.response = self.client().post('/api/v1/auth/login', data=data)
        result = json.loads(self.response.data.decode())
        access_token = result['access_token']
        data = {'name': 'bs1', 'location': 'loc1', 'category': 'cat1'}
        self.response = self.client().post(
                        '/api/v1/businesses', data=data,
                        headers=dict(Authorization="Bearer " + access_token))
        data = {'name': 'updatedbs1', 'location': 'loc1', 'category': 'cat1'}
        self.response = self.client().put(
                        '/api/v1/businesses/1', data=data,
                        headers=dict(Authorization="Bearer " + access_token))
        self.assertTrue(self.response.status_code is 201)

    def test_delete_a_business(self):
        data = {"username": "bsuser",
                "email": "bsuser@email.com",
                "password": "bsuserpass"}
        self.client().post('/api/v1/auth/register', data=data)
        self.response = self.client().post('/api/v1/auth/login', data=data)
        result = json.loads(self.response.data.decode())
        access_token = result['access_token']
        data = {"username": "user1", "password": "user1pass"}
        self.response = self.client().post(
                        '/api/v1/businesses/1', data=data,
                        headers=dict(Authorization="Bearer " + access_token))
        data = {'name': 'updatedbs1', 'location': 'loc1', 'category': 'cat1'}
        self.response = self.client().delete(
                        '/api/v1/businesses/1', data=data,
                        headers=dict(Authorization="Bearer " + access_token))

    def test_retrieve_business_reviews(self):
        self.response = self.client().get('/api/v1/businesses/1/reviews')
        self.assertTrue(self.response.status_code is 200)

    def test_create_business_review(self):
        # Create a user
        data = {"username": "reviewer1",
                "email": "reviewer1@email.com",
                "password": "revpass"}
        self.client().post('/api/v1/auth/register', data=data)
        # Login user
        data = {"username": "reviewer1", "password": "revpass"}
        self.response = self.client().post('/api/v1/auth/login', data=data)
        result = json.loads(self.response.data.decode())
        access_token = result['access_token']
        # Create a business
        data = {'name': 'bs1', 'location': 'loc1', 'category': 'cat3'}
        self.client().post('/api/v1/businesses', data=data,
                           headers=dict(Authorization="Bearer " +
                                                      access_token))

        data = {'content': 'bs1 review'}
        self.response = self.client().post(
                        '/api/v1/businesses/1/reviews', data=data,
                        headers=dict(Authorization="Bearer " + access_token))
        self.assertTrue(self.response.status_code is 201)


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
