from random import choice

ticket_key = (1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')

ticket = []

while len(ticket) < 4:
	random_key = choice(ticket_key)
	if random_key not in ticket:
		ticket.append(random_key)
	
print(f"Any ticket matching these four numbers or letters wins a prize!: \n{ticket}")
