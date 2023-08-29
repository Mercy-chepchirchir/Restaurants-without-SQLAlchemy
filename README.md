# Restaurants-without-SQLAlchemy
Here you will work with three classes: `Restaurant`, `Customer`, and `Review`. The goal is to implement methods that establish relationships between these classes and provide functionality to interact with them.


## Table of content
* Description 
* Installation requirement
* Technology used
* Licence
* Authors info

# DESCRIPTION
## review.py
Here you'll implement methods for the `Review` class that represents reviews written by customers for restaurants.
The `Review` class has attributes for the customer, restaurant, and rating of the review. The `customer` and `restaurant` methods return the corresponding objects. The `rating` method returns the rating. The `all` class method returns a list of all reviews.



## customer.py
Here you will implement methods for the customer class that represents customers who write reviews for restaurants.
The `Customer` class has attributes for the given name and family name of the customer. The `set_given_name` and `set_family_name` methods allow you to update these attributes. The `set_full_name` method combines the given name and family name to create the full name. The `all` class method returns a list of all customer instances.



## restaurant.py
Here you'll implement methods for the `Restaurant` class that represents restaurants and their relationships with customers.
The `Restaurant` class has attributes for the restaurant's name. The `name` method returns the name of the restaurant. The `reviews` method returns a list of reviews for the restaurant, and the `customers` method returns a list of unique customers who reviewed the restaurant.

# INSTALLATION PROCESS
## Frontend
* Git clone the repository to your local machine using the command ` https://github.com/Mercy-chepchirchir/Restaurants-without-SQLAlchemy`
* Navigate to the code challenge directory using `cd Restaurants-without-SQLAlchemy`
* To install the necessary dependencies run `pipenv install`

# TECHNOLOGY USED
python


# LICENSE
MIT license

# AUTHORS INFO
Mercy Chepchirchir

