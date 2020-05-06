prompt = "\nPlease enter your pizza toppings: "
prompt += "\nEnter 'quit' to end the program. "

active = True
toppings = []
while active:
	topping = input(prompt)

	if topping == 'quit':
		active = False
	else:
		toppings.append(topping)
		print(f"\nI'll add {topping} to your pizza.")
		print(f"\nThese are your toppings so far: {toppings}.")