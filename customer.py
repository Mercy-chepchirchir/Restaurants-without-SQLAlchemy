class Customer:
    all_customers = [] #used to store all instances of customer
    
    def __init__(self, given_name, family_name):
        self._given_name= given_name
        self._family_name = family_name
        self._full_name = None
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