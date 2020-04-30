#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
#If you leave out the second argument in the call to get() and the key doesn't exist,
#Python will return the value None.

