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
            
    # the decorator @classmethod defines the class method/indicates that the method is a class
    #  the  method all() takes the class itself as the an argument(cls) method returns all reviews that have been created
    @classmethod
    def all(cls):
        printedReviews = []
        for review in cls.all_reviews:
            printedReviews.append(f"Customer: {review.customer}, Rating: {review.rating}")

        return printedReviews
    
# creating an instance of the review class
myreview = Review("mercy", "Copper Ivy", 12)
newreview = Review("Chirie", "Red Ginger", 10)

# getting the ratings of the reviews using the rating() method
print(myreview.rating)

# getting all the reviews
all_reviews = Review.all()
print(all_reviews)

        
        
        