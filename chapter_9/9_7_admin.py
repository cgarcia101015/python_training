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

	def describe_user(self):
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

class Admin(User):
	"""Model of a User with Amin privileges"""
	def __init__(self, first_name, last_name, age, email, location):
		super().__init__(first_name, last_name, age, email, location)
		self.privileges = ['cand add post','can delete post','can ban user','can suspend user',]

	def show_privileges(self):
		print("Admin Privileges: ")
		admin_privileges = self.privileges
		for privilege in admin_privileges:
			print(f"{privilege}")


# first_user = User('carlos', 'garcia', 35, 'cgarcia101015@gmail.com', 'new york')
new_admin = Admin('cynthia','garcia', 33, 'ccc@gmail.com', 'new york')
new_admin.describe_user()
# new_admin.show_privileges()
# print(first_user.descrive_user())
# print(first_user.greet_user())

# first_user.increment_login_attempts()
# print(first_user.login_attempts)

# first_user.reset_login_attempts()
# print(first_user.login_attempts)