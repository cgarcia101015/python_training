class User:
	"""Model of a users profile"""
	def __init__(self, first_name, last_name, age, email, location):
		"""Initiate attribuetes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.location = location
		self.login_attempts = 0

	def descrive_user(self):
		name = self.first_name + " " + self.last_name
		description = f"Name: {name.title()}\nAge: {self.age}\nEmail: {self.email}\nLocation: {self.location.title()}"
		return description

	def greet_user(self):
		name = self.first_name + " " + self.last_name
		greeting = f"\nHi {name.title()}!"
		return greeting

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0


first_user = User('carlos', 'garcia', 35, 'cgarcia101015@gmail.com', "new york")

print(first_user.descrive_user())
print(first_user.greet_user())

first_user.increment_login_attempts()
print(first_user.login_attempts)

first_user.reset_login_attempts()
print(first_user.login_attempts)