age = 35
print(age >= 30 and age < 25)

favorite_foods = ['pizza', 'burgers', 'hotdogs', 'steaks']
food = 'tacos'

if food not in favorite_foods:
	print(f"\nGotta add {food} to my favorite_foods list.")

food = 'pizza'
if food in favorite_foods:
	print(f"\nI love me some {food}")

print(age >= 30 or age < 25)