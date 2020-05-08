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

print(new_restaurant.restaurant)
print(new_restaurant.cuisine)

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()


