# def descrive_pet(animal_type, pet_name):
# 	"""Display information about a pet."""
# 	print(f"\nI have a {animal_type}.")
# 	print(f"My {animal_type}'s name is {pet_name.title()}.")

# descrive_pet('hamster', 'harry')

# # Multiple function calls
# descrive_pet(animal_type = 'tiger', pet_name = 'tony')

# Default values
def descrive_pet(pet_name, animal_type = 'dog'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

# descrive_pet('hamster', 'harry')

# Multiple function calls
descrive_pet(pet_name = 'willie')
# descrive_pet('willie')