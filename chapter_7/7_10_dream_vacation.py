# Prompt for the person's name and response.
name_prompt = "\nHi, what is your name?"
location_prompt = "\nIf you could visit one place in the world, where would you go?"
ask_again = "Would you like to let another person respond? (yes/ no) "

# Responses will be stored as name:place
responses = {}



while True:
	name = input(name_prompt)
	place = input(location_prompt)

	# Store the response in the dictionary
	responses[name] = place

	# Find out if anyone else is going to take the poll.
	repeat = input(ask_again)
	if repeat != 'yes':
		break

	# Polling is complete. Show the results.
	print("\n--- Poll Results ---")
	for name, place in responses.items():
		print(f"\n{name.title()} would like to visit {place.title()} someday.")