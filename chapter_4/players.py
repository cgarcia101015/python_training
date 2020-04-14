#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#You can include a third value in the brackets indicating a slice. If a third value is 
#included, this tells Python how many items to skip between items in the specified range.


#Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())