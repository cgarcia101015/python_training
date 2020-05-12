class Restaurant:
	"""A model of a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant and cuisine attributes"""
		self.restaurant = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		"""Displays the restaurants name and cuisine type"""
		print(f"Restaurant name: {self.restaurant}")
		print(f"Cuisine type: {self.cuisine}")

	def open_restaurant(self):
		"""Prints a message stating the restaurant is open"""
		print("The restaurant is open.")

new_restaurant = Restaurant('Wendys','fast food')
old_restaurant = Restaurant('Peter Luger','American')
fancy_restaurant = Restaurant('Per Se','gourmet')


new_restaurant.describe_restaurant()
old_restaurant.describe_restaurant()
fancy_restaurant.describe_restaurant()
