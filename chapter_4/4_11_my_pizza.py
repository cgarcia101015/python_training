favorite_pizzas = ['cheese', 'hawiian', 'pepperoni']

for pizza in favorite_pizzas:
	print(f"I like {pizza} pizza!")

print("I really love pizza!")

friend_pizzas = favorite_pizzas[:]
print(friend_pizzas)

favorite_pizzas.append('sausage')
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
	print(pizza)

friend_pizzas.append('anchovies')
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)