from review import Review

class Restaurant:
    def __init__(self,name=None):
        self._name = None
        self._reviews = []
        self._reviewed_customers = []
        if name is not None:
            self.set_name(name)
        
    def set_name (self,name):
        if isinstance (name,str):
            self._name = name
            
    def name (self):
        return self._name
    
    def reviews(self):
        myreviews = []
        for review in Review.all():
            if review.restaurant() == self:
               myreviews.append(review)
        return set(myreviews)     
                
    def customers(self):
        reviewed_customers = []
        for review in Review.all():
            if review.restaurant() == self:
              reviewed_customers.append(review.customer())
        return set(reviewed_customers)
    
    def average_star_rating(self):
        if not self._reviews:
            return 0.0
        total_rating = sum(review.rating for review in self._reviews)
        return total_rating / len(self._reviews)

        
        
     
restaurant1 = Restaurant("Copper Ivy")   
# print(restaurant1.name())
    
# for customer in restaurant1.customers():
#     print(customer)

avg_rating = restaurant1.average_star_rating()
print(f"Average star rating for {restaurant1.name()}: {avg_rating}")