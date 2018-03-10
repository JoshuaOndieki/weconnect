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
            ids = [x for x in app.database['Businesses']]
            if ids:
                business_id = max(ids) + 1
            else:
                business_id = 1
            new_business = Business(business_id, name, location, category, user_id)
            if user_id in app.database['Users']:
                app.database['Businesses'][new_business.id] = new_business.details()
                return (True, 'Success adding business!')
            else:
                return (False, 'No such user!')
        except Exception as e:
                return (False, str(type(e)))

    def edit(self, business_id, name, location, category, user_id):
        """
            Edits and updates business info.

            Arguments:
                data: A dictionary containing
                        business_id, name, location, category, user_id

            Returns:
                A tuple of (True, name, location, category) if success
                updating business, (False, error) otherwise.
        """

        try:
            business = app.database['Businesses'][business_id]
            if business:
                # Update business
                business = app.database['Businesses'][business_id]
                business[0] = name  # Update Name
                business[1] = location  # Update Location
                business[2] = category  # Update Category
                app.database['Businesses'][business_id] = business
                return (True, 'Business update successful!')
        except Exception:
            return (False, 'No business found with given id!')

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
            return (False, str(type(e)))

    def get_business_by_id(self, id):
        try:
            business = app.database['Businesses'][id]
            return (True, {id: business})
        except Exception as e:
            return (False, {'message': str(type(e))})

    def delete_business(self, business_id, user_id):
        """
            Removes a user from the database completely.
            Including related reviews.

            Returns:
                A tuple of (True, success_message) if success deleting business, (False, error) otherwise.
        """

        try:
            self.business = app.database['Businesses'][business_id]
            if self.business[3] == user_id:
                del app.database['Businesses'][business_id]
                # Delete all related reviews.
                all_reviews = app.database['Reviews']
                business_reviews = [x for x in all_reviews if all_reviews[x][1] == business_id]
                for i in business_reviews:
                    del app.database['Reviews'][i]
                return (True, 'Business deleted!')
            return (False, 'Delete request denied!')
        except Exception as e:
            return (False, str(type(e)))
