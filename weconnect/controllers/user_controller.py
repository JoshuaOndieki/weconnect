from weconnect.models.users import User
from weconnect import database


class UserController():
    """
        Controls all CRUD operations of the User object.
    """
    def create_user(self, username, email, password):
        """
            Creates and adds user to the app database.

            Returns:
                A tuple of (True, username) if success adding user, (False, error) otherwise.
        """

        pass

    def login(self, username, password):
        """
            Authenticates and logs in a user.

            Returns:
                A tuple of (True, username) if success logging in user, (False, error) otherwise.
        """

        pass

    def logout(self):
        """
            Logs out a user.

            Returns:
                A tuple of (True) if success logging out user, (False, error) otherwise.
        """

        pass

    def password_reset(self, username, email):
        """
            Resets a user's password by sending a reset code.

            Returns:
                A tuple of (True, username, reset_code) if success resetting user, (False, error) otherwise.
        """

        pass

    def delete_user(self, username):
        """
            Removes a user from the database completely.
            Including related businesses and reviews.

            Returns:
                A tuple of (True) if success deleting user, (False, error) otherwise.
        """

        pass
