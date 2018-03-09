class Review():
    """
        Creates review objects.

        Arguments:
            Review_id: A unique identifier for the review.
            Content: Content of the review.
            Business_id: Id of the business being reviewed.
            User_id: Username of the reviewer.
    """

    def __init__(self, review_id, content, business_id, user_id):
        """
            Review object initializer.

            Returns:
                Object
        """
        self.id = review_id
        self.content = content
        self.business_id = business_id
        self.user_id = user_id

    def details(self):
        return [self.content, self.business_id, self.user_id]
