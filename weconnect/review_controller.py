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
            new_review = Review(review_id, content, business_id, user_id)
            app.database['Reviews'][new_review.id] = new_review.details()
            return (True, "Added review successfully!")
        except Exception as e:
            return (False, str(e))

    def retrieve_reviews(self, business_id):
        """
            Retrieves Review/s for specific business and or user.

            Returns:
                A tuple of (True, [(review_id, content, business_id, user_id)]) if success retrieving reviews, (False, error) otherwise.
        """

        all_reviews = app.database['Reviews']
        business_reviews = [x for x in all_reviews if all_reviews[x][1] == business_id]
        reviews = {}
        for i in business_reviews:
            reviews[i] = app.database['Reviews'][i]
        return (True, reviews)
