from random import randint

class Die:
	"""A model of a Die"""
	def __init__(self, sides=6):
		"""Initialize attributes"""
		self.sides = sides

	def roll_die(self):
		die = self.sides
		roll = randint(1, die)
		print(roll)

six_sided_die = Die()
six_sided_die.roll_die()

ten_sided_die = Die(10)
ten_sided_die.roll_die()

twenty_sided_die = Die(20)
twenty_sided_die.roll_die()




