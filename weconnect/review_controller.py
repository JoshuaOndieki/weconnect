from weconnect.models.reviews import Review
from flask import current_app as app


class ReviewController():
    """
        Controls all CRUD operations of the Review object.
    """

    def create_review(self, content, business_id, user_id):
        """
            Creates and adds a review to the app database.

            Returns:
                A tuple of (True, content) if success adding review,
                (False, error) otherwise.
        """

        try:
            ids = [x for x in app.database['Reviews'].keys()]
            if ids:
                review_id = max(ids) + 1
            else:
                review_id = 1
            self.new_review = Review(review_id, content, business_id, user_id)
            review_details = self.new_review.details()
            app.database['Reviews'][self.new_review.id] = review_details
            return (True, "Added review successfully!")
        except Exception as e:
            return (False, str(type(e)))

    def retrieve_reviews(self, business_id):
        """
            Retrieves Review/s for specific business and or user.

            Returns:
                A tuple of
                (True, [(review_id, content, business_id, user_id)])
                if success retrieving reviews,
                (False, error) otherwise.
        """

        all_reviews = app.database['Reviews']
        self.business_reviews = [x for x in all_reviews
                                 if all_reviews[x][1] == business_id]
        reviews = {}
        for i in self.business_reviews:
            reviews[i] = app.database['Reviews'][i]
        return (True, reviews)
