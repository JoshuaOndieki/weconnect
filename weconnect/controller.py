"""
    This module is a controller for all CRUD operations.
"""
from .models.users import User
from .models.businesses import Business
from .models.reviews import Review
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


class BusinessController():
    """
        Controls all CRUD operations of the Business object.
    """

    def create_business(self, name, location, category):
        """
            Creates and adds a business to the app database.

            Returns:
                A tuple of (True, name) if success adding business, (False, error) otherwise.
        """

        pass

    def edit(self, business_id, name=None, location=None, category=None):
        """
            Edits and updates business info.

            Returns:
                A tuple of (True, name, location, category) if success updating business, (False, error) otherwise.
        """

        pass

    def retrieve_business(self, user_id=None, location=None, category=None):
        """
            Retrieves business/es. Filters if given filter options.

            Returns:
                A tuple of (True, [(business_id, name, location, category, user_id)]) if success retrieving business, (False, error) otherwise.
        """
        pass

    def delete_business(self, business_id):
        """
            Removes a user from the database completely.
            Including related reviews.

            Returns:
                A tuple of (True) if success deleting business, (False, error) otherwise.
        """

        pass


class ReviewController():
    """
        Controls all CRUD operations of the Review object.
    """

    def create_review(self, content, business_id):
        """
            Creates and adds a review to the app database.

            Returns:
                A tuple of (True, content) if success adding review, (False, error) otherwise.
        """

        pass

    def retrieve_review(self, business_id=None, user_id=None):
        """
            Retrieves Review/s for specific business and or user.

            Returns:
                A tuple of (True, [(review_id, content, business_id, user_id)]) if success retrieving reviews, (False, error) otherwise.
        """

        pass
