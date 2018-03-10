class Business():
    """
        Creates Business objects.

        Arguments:
            Id: A unique identifier for the business.
            Name: Name of the business.
            Location: Place where the business is situated.
            Category: Area of focus of the business.
            user_id: Username of the business creater.
    """

    def __init__(self, business_id, name, location, category, user_id):
        """
            Business object initializer.

            Returns:
                Object
        """
        self.id = business_id
        self.name = name
        self.location = location
        self.category = category
        self.user_id = user_id

    def details(self):
        return([self.name, self.location, self.category, self.user_id])
