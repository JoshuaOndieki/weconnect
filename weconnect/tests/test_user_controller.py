import unittest
from weconnect.user_controller import UserController
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
        self.response = self.user.create_user(
                                            'test_user0',
                                            'test_user0@email.com',
                                            'password')
        self.assertTrue(self.response[1] == 'User creation successful!',
                        msg='Should return success msg if user is \
                        created successfully!')

    def test_does_not_create_duplicate_username(self):
        self.response = self.user.create_user('to_be_duplicated',
                                              'dup@email.com',
                                              'duppassword')
        self.response = self.user.create_user('to_be_duplicated',
                                              'dup1@email.com',
                                              'password')
        self.assertTrue(self.response[1] == 'Username exists!',
                        msg='Should not allow reusability of \
                         usernames!')

    def test_does_not_create_duplicate_email(self):
        self.response = self.user.create_user('to_be_duplicated1',
                                              'dup3@email.com',
                                              'duppassword')
        self.response = self.user.create_user('to_be_duplicated2',
                                              'dup3@email.com',
                                              'duppassword')
        self.assertFalse(self.response[1] == 'User email exists!',
                         msg='Should not allow reusability of emails!')

    def test_login_success_with_correct_info(self):
        self.user.create_user('right_user',
                              'right_user@email.com',
                              'password')
        self.response = self.user.login('right_user', 'password')
        self.assertTrue(self.response[1] == 'User login success!',
                        msg='Should login a user given the correct \
                        credentials!')

    def test_login_fails_with_non_user(self):
        self.response = self.user.login('non_user', 'fake_password')
        self.assertFalse(self.response[1] == 'User does not exist!',
                         msg='Should deny login with non user!')

    def test_login_fails_with_wrong_password(self):
        self.user.create_user('wrong_pass_user',
                              'wpass_user@email.com',
                              'password')
        self.response = self.user.login('wrong_pass_user', 'guess_pass')
        self.assertTrue(self.response[1] == 'Wrong password!',
                        msg='Should deny wrong credentials!')

    def test_find_user_by_username(self):
        self.user.create_user('founder',
                              'founder_user@email.com',
                              'password')
        self.response = self.user.find_by_username('founder')
        self.assertTrue(self.response[0])

    def test_find_user_by_non_existing_username(self):
        self.response = self.user.find_by_username('non_user')
        self.assertFalse(self.response[0])

    def test_reset_password(self):
        self.user.create_user('forgetter',
                              'forgetter@email.com',
                              'oldpass')
        self.response = self.user.password_reset('forgetter', 'oldpass', 'newpass')
        self.assertTrue(self.response[0], msg='')


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
