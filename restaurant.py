from review import Review
from customer import Customer

class Restaurant:
    def __init__(self,name=None):
        self._name = None
        self._reviews = []
        if name is not None:
            self.set_name(name)
        
    def set_name (self,name):
        if isinstance (name,str):
            self._name = name
            
    def name (self):
        return self._name
    
    def reviews(self):
        return self._reviews
    
    def add_review(self, customer, rating):
        self._reviews.append(Review(customer, self, rating))
    
    
     
restaurant1 = Restaurant("Copper Ivy")   
# print(restaurant1.name())

customer1 = Customer("Mercy", "Tonui")

restaurant1.add_review(customer1, 8)
restaurant1.add_review(customer1, 4)

for review in restaurant1.reviews():
    print(review.rating)
        