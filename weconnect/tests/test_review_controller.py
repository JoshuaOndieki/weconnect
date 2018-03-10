import unittest
from weconnect.review_controller import ReviewController
from weconnect.user_controller import UserController
from weconnect.business_controller import BusinessController
from weconnect import create_app


class TestReviewController(unittest.TestCase):

    def setUp(self):
        self.review = ReviewController()
        self.user = UserController()
        self.business = BusinessController()
        self.app = create_app(config_name='testing')
        self.context = self.app.app_context()
        self.context.push()

        self.business.create_business("Business Name", "bs, location", "bs cat", 'test_user')
        self.user.create_user(
                            'test_user',
                            'test_user@email.com',
                            'password')

    def tearDown(self):
        self.context.pop()

    def test_create_review(self):
        self.response = self.review.create_review("Review content", 1, 1)
        self.assertTrue(self.response[0], msg="Should create a business review successfully!")

    def test_retrieve_reviews_by_business_id(self):
        self.review.create_review("Review content", 1, 1)
        self.response = self.review.retrieve_reviews(1)
        self.assertTrue(self.response[0], msg="Should retrieve reviews by business id correctly!")


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
