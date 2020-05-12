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