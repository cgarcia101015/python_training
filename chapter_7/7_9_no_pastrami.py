
sandwich_orders = ['veggie', 'pastrami', 'grilled cheese', 'pastrami', 'turkey', 'pastrami', 'roast beef']
finished_sandwiches = []

print('The Deli has run out of pastrami.')

while 'pastrami' in sandwich_orders:
		sandwich_orders.remove('pastrami')

while sandwich_orders:
	

    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")