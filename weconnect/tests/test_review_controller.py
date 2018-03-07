import unittest
from weconnect.controllers.review_controller import ReviewController
from weconnect import database


class TestReviewController(unittest.TestCase):

    def setUp(self):
        self.review = ReviewController()

    def test_create_review(self):
        database["Current user"] = "test_user"  # Manual login
        database["Businesses"][200] = ["Business200 Name", "Bs200, Location", "bs200 Cat", "test_user"]  # Manual add business
        self.response = self.review.create_review("Review content", 200)
        self.assertTrue(self.response[0], msg="Should create a business review successfully!")

    def test_retrieve_reviews_by_business_id(self):
        self.response = self.review.retrieve_review(business_id=200)
        self.assertNotEqual(self.response[1], 0, msg="Should retrieve reviews by business id correctly!")

    def test_retrieve_reviews_by_user_id(self):
        self.response = self.review.retrieve_review(user_id="test_user")
        self.assertNotEqual(self.response[1], 0, msg="Should retrieve reviews by user id correctly!")


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
