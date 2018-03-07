import unittest
from weconnect.controllers.business_controller import BusinessController
from weconnect import database


class TestBusinessController(unittest.TestCase):

    def setUp(self):
        self.business = BusinessController()

    def test_creates_business(self):
        database["Current user"] = "test_user"  # Manually login user
        self.response = self.business.create_business("Business Name", "bs, location", "bs cat")
        self.business.create_business("Business2 Name", "bs2, location", "bs2 cat")
        self.businesses = [x for x in database["Businesses"].values()]
        self.assertTrue(self.response[0] and ["Business Name", "bs, location", "bs cat"] in self.businesses, msg="Should add a business to the app database successfully!")

    def test_does_not_create_business_without_login(self):
        database["Current user"] = ""  # Manually logout user
        self.response = self.business.create_business("Business1 Name", "bs1, location", "bs2 cat")
        self.assertFalse(self.response[0], msg="Deny business creation if user not logged in!")

    def test_retrieve_all_businesses(self):
        self.response = self.business.retrieve_business()
        self.assertTrue(self.response[0] and len(self.response[1]) is not 0, "Should return a list of businesses!")

    def test_retrieve_businesses_by_user(self):
        self.response = self.business.retrieve_business(user_id="test_user")
        self.assertNotEqual(self.response[1], 0, msg="Should return a list of businesses")
        # business_user_ids = [x[4] for x in self.response[1]]
        # ids_check = lambda l: all(x == l[0] for x in l)
        # self.assertTrue(ids_check(business_user_ids))

    def test_update_business(self):
        database["Current user"] = "test_user"  # Manual login
        database["Businesses"][911] = ["Business Name not updated", "Bs, Location", "bs Cat", "test_user"]  # Manual add business
        self.response = self.business.edit(business_id=911, name="Business Name updated", location="bs, Location", category="bs, Cat")
        self.assertTrue(self.response[0], msg="Should update a business info!")

    def test_can_not_delete_business_if_not_owner(self):
        database["Current user"] = "fake_owner"
        self.response = self.business.delete_business(911)
        self.assertFalse(self.response[0], msg="Should allow only owners to delete the business!")

    def test_delete_a_business(self):
        database["Current user"] = "test_user"
        self.response = self.business.delete_business(911)
        self.assertTrue(self.response[0] and 911 not in database["Businesses"].keys(), msg="Should delete a business from the database!")


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
