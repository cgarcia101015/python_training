prompt = "\nWant a theater ticket?"
prompt += "\nPlease enter your age: "



while True:
	age = input(prompt)

	if age == 'quit':
		break
	age = int(age)

	if age < 3:
		print("\nYour ticket is free.")
		
	elif age < 13:
		print("\nYour ticket is $10")
		
	else:
		print("\nYour ticket is $15")
		

