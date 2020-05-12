"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kwh battery")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initailize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()
		# self.battery_size = 75

	# def describe_battery(self):
	# 	"""Print a statement describing the battery size."""
	# 	print(f"This car has a {self.battery_size}-kwh battery.")


# my_tesla = ElectricCar('tesla','model s', 2019)
# print(my_tesla.get_descriptive_name())
# # my_tesla.describe_battery()
# my_tesla.battery.describe_battery()
# my_tesla.batteryd.get_range()

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# # # Modifying an attribute's value directly
# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer()

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# my_new_car.update_odometer(10)
# my_new_car.read_odometer()
