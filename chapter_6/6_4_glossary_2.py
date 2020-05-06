glossary = {'mutable': 'values that cannot be changed',
	'floats': 'a number with a decimal point',
	'constants': 'like a variable whose value stays the same throughout the life of a program',
	'insert()': 'adds a new element at any position in your list',
	'len()': 'finds the length of a list',}

for key, value in glossary.items():
	print(f"\n{key.title()}:")
	print(f"{value}")