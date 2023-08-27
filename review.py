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
   
    # set_rating method allows rating only if the provided value is an integer
    def set_rating(self, rating):
        if isinstance (rating,int):
            self._rating = rating
            
        else:
            print("Rating must be an integer")
            
     # return the rating
    def get_rating(self):
        return self._rating   
     
    
    rating = property(get_rating, set_rating)
            
   