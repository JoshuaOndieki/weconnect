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
            return (False, "Username exists!")

        # Get emails
        self.emails = [x[0] for x in app.database['Users'].values()]
        if app.database["Users"] and email in self.emails:
            return (False, "Email exists!")
        self.new_user = User(username, email, password)
        app.database["Users"][self.new_user.username] = self.new_user.credentials()
        return (True, 'User creation successful!')

    def login(self, username, password):
        """
            Authenticates and logs in a user.

            Returns:
                A tuple of (True, username) if success logging in user, (False, error) otherwise.
        """
        try:
            self.user_password = app.database['Users'][username][1]
            if self.user_password == password:
                return (True, 'User login success!')
            return (False, 'Wrong password!')
        except KeyError:
            return (False, 'No such user!')

    def find_by_username(self, username):
        try:
            self.user = app.database["Users"][username]
            return (True, self.user)
        except KeyError:
            return (False,)

    def password_reset(self, username, password, new_password):
        """
            Resets a user's password.

            Returns:
                A tuple of (True, username) if success resetting user, (False, error) otherwise.
        """

        try:
            self.user_password = app.database['Users'][username][1]
        except Exception as e:
            return (False, str(type(e)))
        if self.user_password == password:
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
