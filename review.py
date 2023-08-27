class Review:
# all reviews is an empty list so that it will be used to store all instances of reviews.
    all_reviews = [] 
    
    def __init__ (self, customer, restaurant, rating=None):
        self.customer = customer
        self.restaurant = restaurant
        self._rating = None
        Review.all_reviews.append(self)  # Adding the review to the all_reviews list

        if rating is not None:
            self.set_rating(rating)
  