#A dictionary of similar objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
# 	print(f"{name.title()}'s favorite language is {language.title()}.")

#Looping through all the keys in a dictionary
# for name in favorite_languages.keys():
# 	print(name.title())
# or 

# for name in favorite_languages:
# 	print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages:
# 	print(f"Hi {name.title()}.")

# 	if name in friends:
# 		language = favorite_languages[name].title()
# 		print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
# 	print("Erin, please take our poll!")

#Looping through a dictionary's keys in a particular order
# for name in sorted(favorite_languages.keys()):
# 	print(f"{name.title()}, thank you for taking the poll.")

#Looping through all the values in a dictionary

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
# 	print(language.title())

#Looping through all the unique values in a dictionary

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
# 	print(language.title())


polsters = ['phil', 'sarah', 'edward', 'fred', 'bob', 'ted']

for name in polsters:
	print(f"Hi {name.title()}.")

	if name in favorite_languages:
		language = favorite_languages[name].title()
		print(f"\tThank you for responding!")
	elif name not in favorite_languages:
		
		print(f"\tYou should take the poll!")
































