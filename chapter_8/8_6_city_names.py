def city_country(city_name, country_name):
	place = f"{city_name}, {country_name}"
	return place.title()

named_place = city_country('sao paolo', 'brazi')
print(named_place)

named_place = city_country('dublin', 'ireland')
print(named_place)

named_place = city_country('madrid', 'spain')
print(named_place)