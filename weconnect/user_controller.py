from weconnect.models.users import User
from flask import current_app as app


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

        if app.database["Users"] and username in app.database["Users"]:
            return (False, "User exists!")
        new_user = User(username, email, password)
        app.database["Users"][new_user.username] = new_user.credentials()
        print("--------------------------")
        print(app.database)
        print("--------------------------")
        return (True, new_user.username)

    def login(self, username, password):
        """
            Authenticates and logs in a user.

            Returns:
                A tuple of (True, username) if success logging in user, (False, error) otherwise.
        """

        pass

    def find_by_username(self, username):
        try:
            user = app.database["Users"][username]
            return user
        except KeyError:
            return False

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
