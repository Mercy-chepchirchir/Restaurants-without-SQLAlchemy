from review import Review
from customer import Customer

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
        return self._reviews
    
    def add_review(self, customer, rating):
        self._reviews.append(Review(customer, self, rating))
        
        # check if the customer passed in as argument when creating review exists in list of reviewed customers
        if not any(rev_customer.full_name == customer.full_name for rev_customer in self._reviewed_customers):
            self._reviewed_customers.append(customer)
            
                
    def customers(self):
        return self._reviewed_customers
        
     
restaurant1 = Restaurant("Copper Ivy")   
# print(restaurant1.name())

customer1 = Customer("Mercy", "Tonui")
customer2 = Customer("Potato", "Chips")

restaurant1.add_review(customer1, 8)
restaurant1.add_review(customer1, 4)
restaurant1.add_review(customer2, 10)

# for review in restaurant1.reviews():
#     print(review.rating)
    
for customer in restaurant1.customers():
    print(customer)