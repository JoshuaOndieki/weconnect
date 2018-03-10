import unittest
from weconnect.business_controller import BusinessController
from weconnect.user_controller import UserController
from weconnect import create_app


class TestBusinessController(unittest.TestCase):

    def setUp(self):
        self.business = BusinessController()
        self.user = UserController()
        self.app = create_app(config_name='testing')
        self.context = self.app.app_context()
        self.context.push()

        self.user.create_user(
                            'test_user',
                            'test_user@email.com',
                            'password')

    def tearDown(self):
        self.context.pop()

    def test_creates_business(self):
        self.response = self.business.create_business(
                        "Business Name",
                        "bs, location", "bs cat", 'test_user')
        self.assertTrue(
                        self.response[1] == 'Success adding business!', msg="Should add a business to the app database \
                        successfully!")

    def test_does_not_create_business_with_non_user(self):
        self.response = self.business.create_business(
                        "Business1 Name",
                        "bs1, location", "bs2 cat", 'non_user')
        self.assertFalse(
                        self.response[0],
                        msg="Deny business creation if user not logged \
                        in!")

    def test_retrieve_all_businesses(self):
        self.response = self.business.get_businesses()
        self.assertTrue(
                        self.response[0],
                        msg="Should return a list of businesses!")

    def test_retrieve_businesses_by_id(self):
        self.business.create_business(
                                      "Business iName",
                                      "bs, location", "bs cat", 'test_user')
        self.response = self.business.get_business_by_id(3)
        self.assertTrue(
                        self.response[0],
                        msg="Should return a business by id")

    def test_update_business(self):
        self.business.create_business(
                                      "Business uName",
                                      "bs, location", "bs cat",
                                      'test_user')
        self.response = self.business.edit(
                        3, "Business Name updated",
                        "bs, Location", "bs, Cat", 'test_user')
        self.assertTrue(self.response[0], msg="Should update a business info!")

    def test_delete_a_business(self):
        self.business.create_business(
                                      "Business2 Name",
                                      "bs2, location", "bs2 cat",
                                      'test_user')
        self.response = self.business.delete_business(1, 'test_user')
        self.assertTrue(
                        self.response[0],
                        msg="Should delete a business from the \
                        database!")


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
