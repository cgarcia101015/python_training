buffet_foods = ('crab legs', 'rice', 'salads', 'chicken', 'eggrolls')

for food in buffet_foods:
	print(food)

# buffet_foods[0] = 'noodles' --> TypeError

buffet_foods = ('crab legs', 'rice', 'ribs', 'soup', 'eggrolls')
print("Revised menu:")
for food in buffet_foods:
	print(food)
