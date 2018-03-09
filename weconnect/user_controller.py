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
        return (True, new_user.username)

    def login(self, username, password):
        """
            Authenticates and logs in a user.

            Returns:
                A tuple of (True, username) if success logging in user, (False, error) otherwise.
        """

        user_password = app.database['Users'][username][1]
        if user_password == password:
            return (True, username)
        return (False, 'Wrong username or password!')

    def find_by_username(self, username):
        try:
            user = app.database["Users"][username]
            return user
        except KeyError:
            return False

    def logout(self, token):
        """
            Logs out a user by adding access token to blacklist.

            Returns:
                A tuple of (True) if success logging out user, (False, error) otherwise.
        """
        if token not in app.database['log']['token_blacklist']:
            app.database['log']['token_blacklist'].append(token)
            return (True, 'Logout successful!')
        return (False, 'User was already logged out!')

    def password_reset(self, username, password, new_password):
        """
            Resets a user's password.

            Returns:
                A tuple of (True, username) if success resetting user, (False, error) otherwise.
        """

        try:
            user_password = app.database['Users'][username][1]
        except Exception as e:
            return (False, str(e))
        if user_password == password:
            # set new password
            app.database['Users'][username][1] = new_password
            return (True, 'Success resetting password!')
        return (False, 'Invalid credentials!')

    def delete_user(self, username):
        """
            Removes a user from the database completely.
            Including related businesses and reviews.

            Returns:
                A tuple of (True) if success deleting user, (False, error) otherwise.
        """

        pass
