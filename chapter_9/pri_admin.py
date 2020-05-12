from user import User
class Privileges:
	"""A class storing admin privilages"""
	def __init__(self):
		"""Initialize attributes"""
		self.privileges = ['can add post','can delete post','can ban user','can suspend user',]


	def show_privileges(self):
		print("Admin Privileges: ")
		admin_privileges = self.privileges

		for privilege in admin_privileges:
			print(f"{privilege}")


class Admin(User):
	"""Model of a User with Admin privileges"""
	def __init__(self, first_name, last_name, age, email, location):
		super().__init__(first_name, last_name, age, email, location)
		self.admin = Privileges()