from weconnect.models.businesses import Business
from flask import current_app as app


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
