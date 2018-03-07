from weconnect.models.reviews import Review
from weconnect import database


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
