class Restaurant:
	"""A model of a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant and cuisine attributes"""
		self.restaurant = restaurant_name.title()
		self.cuisine = cuisine_type
		self.number_served = 0 

	def describe_restaurant(self):
		"""Displays the restaurants name and cuisine type"""
		print(f"Restaurant name: {self.restaurant}")
		print(f"Cuisine type: {self.cuisine}")

	def open_restaurant(self):
		"""Prints a message stating the restaurant is open"""
		print("The restaurant is open.")

	def set_number_served(self, customer_served):
		self.number_served = customer_served

	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served."""
		self.number_served += additional_served

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))

# new_restaurant = Restaurant('Wendys','fast food',432)

# print(new_restaurant.restaurant)
# print(new_restaurant.cuisine)

# new_restaurant.describe_restaurant()
# new_restaurant.open_restaurant()
