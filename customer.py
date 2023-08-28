from review import Review
from restaurant import Restaurant

class Customer:
    all_customers = [] #used to store all instances of customer
    
    def __init__(self, given_name, family_name):
        self._given_name= given_name
        self._family_name = family_name
        self._full_name = None
        self._reviews = []
        self._restaurants = []
        Customer.set_full_name(self)
        Customer.all_customers.append(self)
        
    def set_given_name(self,given_name):
        if isinstance (given_name,str):
            self._given_name = given_name
            
    def get_given_name(self):
        return self._given_name
        
    given_name =property(get_given_name,set_given_name)
                  
    def set_family_name(self,family_name):
        if isinstance (family_name,str):
            self._family_name = family_name
            
    def get_family_name(self):
        return self._family_name
        
    family_name =property(get_family_name,set_family_name)
            
# creates full name by combining the given name and family name
    def set_full_name(self):
        self._full_name = f"{self._given_name} {self._family_name}"
    
    def get_full_name(self):
        return self._full_name
    
    full_name = property(get_full_name, set_full_name)
    
    def restaurants(self):
        reviewed_restaurants = []
        for review in Review.all():
            if review.customer() == self:
                reviewed_restaurants.append(review.restaurant())
        return set(reviewed_restaurants)
                
    def add_review(self, restaurant, rating):
        new_review = Review(self._full_name, restaurant.name(), rating)
        self._reviews.append(new_review)            
        restaurant._reviews.append(new_review)
        
    def num_reviews(self):
        return len(self._reviews)


    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name == name:
                return customer
        return None
    
    
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.full_name.split()[0] == name:
                matching_customers.append(customer)
        return matching_customers
            
# the all class method returns the list of all customer instances          
    @classmethod
    def all(cls):
        return cls.all_customers
            
    def __str__(self):
        return self._full_name
    
mycustomer = Customer("Mercy", "Tonui")
newCustomer = Customer("Mercy", "Chepchirchir")



# printing customer information
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name)
       

print(all_customers)
print(mycustomer)


restaurant1 = Restaurant("Cooper VY")

customer1 = Customer("Chiri", "Tonui")
customer1.add_review(restaurant1, 7)

for review in restaurant1.reviews():
    print(review.rating)
