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

class IceCreamStand(Restaurant):
	"""A model of a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes of the parent class"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla','chocolate','strawberry','mint chip']

	def describe_ice_cream_stand(self):
		"""Display the ice cream stands name, cuisine type and flavors"""
		ic_stand = f"Name: {self.restaurant}\nCuisine Type: {self.cuisine}\nFlavors served: {self.flavors}"
		return ic_stand


# new_restaurant = Restaurant('Wendys','fast food')
ice_cream_restaurant = IceCreamStand("Joe's Ice Cream Shop", "desert")

print(ice_cream_restaurant.describe_ice_cream_stand())
# print(new_restaurant.restaurant)
# print(new_restaurant.cuisine)

# new_restaurant.describe_restaurant()
# new_restaurant.open_restaurant()