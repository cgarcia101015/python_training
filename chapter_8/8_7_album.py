def make_album(artist_name, album_title, num_of_songs = ''):
	"""Return a dictionary of information about an artist"""
	if num_of_songs:
			album = {'artist': artist_name, 'album': album_title, 'number of songs': num_of_songs}
	else:
		album = {'artist': artist_name, 'album': album_title}

	return album

picked_album = make_album('micheal jackson', 'bad')
print(picked_album)

picked_album = make_album('metallica', 'master of puppets')
print(picked_album)

picked_album = make_album('micheal jackson', 'thriller')
print(picked_album)

picked_album = make_album('drake', 'scorpion', '97')
print(picked_album)


















# def build_person(first_name, last_name, age = None):
# 	"""Return a dictionary of information about a person."""
# 	person = {'first': first_name, 'last': last_name}
# 	if age:
# 		person['age'] = age
# 	return person

# musician = build_person('jimi', 'hendrix', age = 27)
# print(musician)