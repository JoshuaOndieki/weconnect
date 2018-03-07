
import unittest
from weconnect.models.users import User
from weconnect.models.businesses import Business
from weconnect.models.reviews import Review


class TestModels(unittest.TestCase):
    """
        This module tests creation of instances.
    """
    def test_user_instance_creation(self):
        self.user_instance = User("test_user", "test_user@email.com", "test password")
        self.assertIsInstance(self.user_instance, User, msg="Instance created should be a User instance!")

    def test_business_instance_creation(self):
        self.business_instance = Business(1, "test Business", "Nairobi, Kenya", "test category", "test_user")
        self.assertIsInstance(self.business_instance, Business, msg="Instance created should be a Business instance!")

    def test_review_instance_creation(self):
        self.review_instance = Review(1, "review content", 1, "test_user")
        self.assertIsInstance(self.review_instance, Review, msg="Instance created should be a Review instance!")


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
