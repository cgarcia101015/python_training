def make_car(
		manufacturer,model,
		**car_info):
	"""Build a dictionary containin˜g everything we know about a car"""
	car_info['manufacturer'] = 'manufacturer'
	car_info['model'] = 'model'
	return car_info

new_car = make_car('toyota','supra',
				  color='red',
				  sport_exhaust=True)

print(new_car)