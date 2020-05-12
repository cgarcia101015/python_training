class User:
	"""Model of a users profile"""
	def __init__(self, first_name, last_name, age, email, location):
		"""Initiate attribuetes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.location = location

	def descrive_user(self):
		name = self.first_name + " " + self.last_name
		description = f"Name: {name.title()}\nAge: {self.age}\nEmail: {self.email}\nLocation: {self.location.title()}"
		return description

	def greet_user(self):
		name = self.first_name + " " + self.last_name
		greeting = f"\nHi {name.title()}!"
		return greeting


first_user = User('carlos', 'garcia', 35, 'cgarcia101015@gmail.com', "new york")

print(first_user.descrive_user())
print(first_user.greet_user())

second_user = User('cynthia', 'garcia', 33, 'cyncyn@gmail.com', "new york")

print(second_user.descrive_user())
print(second_user.greet_user())

third_user = User('lucas', 'garcia', 1, 'lucas@gmail.com', "new york")

print(third_user.descrive_user())
print(third_user.greet_user())