from weconnect.models.businesses import Business
from flask import current_app as app


class BusinessController():
    """
        Controls all CRUD operations of the Business object.
    """

    def create_business(self, name, location, category, user_id):
        """
            Creates and adds a business to the app database.

            Returns:
                A tuple of (True, name) if success adding business, (False, error) otherwise.
        """
        try:
            ids = [x for x in app.database['Businesses'].keys()]
            if ids:
                business_id = max(ids) + 1
            else:
                business_id = 1
            new_business = Business(business_id, name, location, category, user_id)
            app.database['Businesses'][new_business.id] = new_business.details()
            return (True, name)
        except Exception as e:
            return (False, str(e))

    def edit(self, data):
        """
            Edits and updates business info.

            Arguments:
                data: A dictionary containing
                        business_id, name, location, category

            Returns:
                A tuple of (True, name, location, category) if success
                updating business, (False, error) otherwise.
        """

        try:
            if data['id'] in app.database['Businesses']:
                # Update business
                business = app.database['Businesses'][data['id']]
                business[0] = data['name']  # Update Name
                business[1] = data['location']  # Update Location
                business[2] = data['category']  # Update Category
                app.database['Businesses'][data['id']] = business
                return (True, 'Business update successful!')
            return (False, 'No business found with given id!')
        except Exception as e:
            return (False, str(e))

    def get_businesses(self):
        """
            Retrieves businesses. Filters if given filter options.

            Returns:
                A tuple of
                (True, {business_id: [name, location, category, user_id]})
                if success retrieving businesses,
                (False, error) otherwise.
        """
        try:
            return (True, app.database['Businesses'])
        except Exception as e:
            return (False, str(e))

    def get_business_by_id(self):
        pass

    def delete_business(self, business_id):
        """
            Removes a user from the database completely.
            Including related reviews.

            Returns:
                A tuple of (True) if success deleting business, (False, error) otherwise.
        """

        pass
