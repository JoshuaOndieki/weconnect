import unittest
from weconnect.controller import UserController, BusinessController, ReviewController
from weconnect import database


class TestUserController(unittest.TestCase):

    def test_creates_user(self):
        self.response = self.test_user = UserController("test_user", "test_user@email.com", "password")
        self.assertTrue(self.response[0] and "test_user" in database["Users"], msg="Should return True if user is successfully added to the app database!")

    def test_does_not_create_duplicate_username(self):
        self.response = self.to_be_duplicated_user = UserController("to_be_duplicated", "dup@email.com", "duppassword")
        self.assertTrue(self.response[0], msg="Creates user successfully at first.")
        self.response = self.duplicate_user = UserController("to_be_duplicated", "dup1@email.com", "password")
        self.assertFalse(self.response[0], msg="Should not allow reusability of usernames!")

    def test_does_not_create_duplicate_email(self):
        self.response = self.to_be_duplicated_user = UserController("to_be_duplicated1", "dup3@email.com", "duppassword")
        self.assertTrue(self.response[0], msg="Creates user successfully at first.")
        self.response = self.duplicate_user = UserController("to_be_duplicated2", "dup3@email.com", "duppassword")
        self.assertFalse(self.response[0], msg="Should not allow reusability of emails!")

    def test_login_success_with_correct_info(self):
        self.response = UserController.login("test_user", "password")
        self.assertTrue(self.response[0], msg="Should login a user given the correct credentials!")
        self.assertTrue(database["Current user"] is "test_user", msg="User session should be saved to a database log!")

    def test_login_fails_with_wrong_data(self):
        self.response = UserController.login("test_user", "fake_password")
        self.assertFalse(self.response[0], msg="Should deny login with unmatching user credentials!")

    def test_logs_out_current_user(self):
        self.response = UserController.logout()
        self.assertTrue(self.response[0] and not database["Current user"], msg="Should logout user and remove from session log!")


class TestBusinessController(unittest.TestCase):

    def test_creates_business(self):
        database["Current user"] = "test_user"  # Manually login user
        self.response = BusinessController.create_business("Business Name", "bs, location", "bs cat")
        BusinessController.create_business("Business2 Name", "bs2, location", "bs2 cat")
        self.businesses = [x for x in database["Businesses"].values()]
        self.assertTrue(self.response[0] and ["Business Name", "bs, location", "bs cat"] in self.businesses, msg="Should add a business to the app database successfully!")

    def test_does_not_create_business_without_login(self):
        database["Current user"] = ""  # Manually logout user
        self.response = BusinessController.create_business("Business1 Name", "bs1, location", "bs2 cat")
        self.assertFalse(self.response[0], msg="Deny business creation if user not logged in!")

    def test_retrieve_all_businesses(self):
        self.response = BusinessController.retrieve_business()
        self.assertTrue(self.response[0] and len(self.response[1]) is not 0, "Should return a list of businesses!")

    def test_retrieve_businesses_by_user(self):
        self.response = BusinessController.retrieve_business(user_id="test_user")
        self.assertNotEqual(self.response[1], 0, msg="Should return a list of businesses")
        # business_user_ids = [x[4] for x in self.response[1]]
        # ids_check = lambda l: all(x == l[0] for x in l)
        # self.assertTrue(ids_check(business_user_ids))

    def test_update_business(self):
        database["Current user"] = "test_user"  # Manual login
        database["Businesses"][911] = ["Business Name not updated", "Bs, Location", "bs Cat", "test_user"]  # Manual add business
        self.response = BusinessController.edit(business_id=911, name="Business Name updated", location="bs, Location", category="bs, Cat")
        self.assertTrue(self.response[0], msg="Should update a business info!")

    def test_can_not_delete_business_if_not_owner(self):
        database["Current user"] = "fake_owner"
        self.response = BusinessController.delete_business(911)
        self.assertFalse(self.response[0], msg="Should allow only owners to delete the business!")

    def test_delete_a_business(self):
        database["Current user"] = "test_user"
        self.response = BusinessController.delete_business(911)
        self.assertTrue(self.response[0] and 911 not in database["Businesses"].keys(), msg="Should delete a business from the database!")


class TestReviewController(unittest.TestCase):

    def test_create_review(self):
        database["Current user"] = "test_user"  # Manual login
        database["Businesses"][200] = ["Business200 Name", "Bs200, Location", "bs200 Cat", "test_user"]  # Manual add business
        self.response = ReviewController.create_review("Review content", 200)
        self.assertTrue(self.response[0], msg="Should create a business review successfully!")

    def test_retrieve_reviews_by_business_id(self):
        self.response = ReviewController.retrieve_review(business_id=200)
        self.assertNotEqual(self.response[1], 0, msg="Should retrieve reviews by business id correctly!")

    def test_retrieve_reviews_by_user_id(self):
        self.response = ReviewController.retrieve_review(user_id="test_user")
        self.assertNotEqual(self.response[1], 0, msg="Should retrieve reviews by user id correctly!")


if __name__ is "__main__":
    unittest.main()
