import unittest
from weconnect.user_controller import UserController
from weconnect import database
from weconnect import create_app


class TestUserController(unittest.TestCase):

    def setUp(self):
        self.user = UserController()
        self.app = create_app(config_name='testing')
        self.context = self.app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_creates_user(self):
        self.response = self.user.create_user("test_user", "test_user@email.com", "password")
        self.assertTrue(self.response[0] and "test_user" in database["Users"], msg="Should return True if user is successfully added to the app database!")

    def test_does_not_create_duplicate_username(self):
        self.response = self.user.create_user("to_be_duplicated", "dup@email.com", "duppassword")
        self.assertTrue(self.response[0], msg="Creates user successfully at first.")
        self.response = self.user.create_user("to_be_duplicated", "dup1@email.com", "password")
        self.assertFalse(self.response[0], msg="Should not allow reusability of usernames!")

    def test_does_not_create_duplicate_email(self):
        self.response = self.user.create_user("to_be_duplicated1", "dup3@email.com", "duppassword")
        self.assertTrue(self.response[0], msg="Creates user successfully at first.")
        self.response = self.user.create_user("to_be_duplicated2", "dup3@email.com", "duppassword")
        self.assertFalse(self.response[0], msg="Should not allow reusability of emails!")

    def test_login_success_with_correct_info(self):
        self.response = self.user.login("test_user", "password")
        self.assertTrue(self.response[0], msg="Should login a user given the correct credentials!")
        self.assertTrue(database["log"]["current_user"] is "test_user", msg="User session should be saved to a database log!")

    def test_login_fails_with_wrong_data(self):
        self.response = self.user.login("test_user", "fake_password")
        self.assertFalse(self.response[0], msg="Should deny login with unmatching user credentials!")

    def test_logs_out_current_user(self):
        self.response = self.user.logout()
        self.assertTrue(self.response[0] and not database["log"]["current_user"], msg="Should logout user and remove from session log!")


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
