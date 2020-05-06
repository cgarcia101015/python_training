user_num = input("Please enter a whole number: ")

user_num = int(user_num)

if user_num % 10 == 0:
	print(f"{user_num} is a mulitple of 10.")
else:
	print(f"{user_num} is not a mulitple of 10.")