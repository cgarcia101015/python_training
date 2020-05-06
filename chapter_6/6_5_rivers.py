rivers = {'amazon': 'brazil',
	'nile': 'egypt',
	'mississippi': 'united states',
	}

for river, country in rivers.items():
	print(f"\nThe {river.title()} runs through {country.title()}.")