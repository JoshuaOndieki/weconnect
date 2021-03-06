class User():
    """
        Creates user objects.

        Arguments:
            Username: A unique alias for the user.
            Email: Personal email of the user.
            Password: A secret security key.
    """

    def __init__(self, username, email, password):
        """
            User object initializer.

            Returns:
                Object
        """
        self.username = username
        self.email = email
        self.password = password

    def credentials(self):
        return [self.email, self.password]
