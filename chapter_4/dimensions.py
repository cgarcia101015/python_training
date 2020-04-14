#Defining a tuple
dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# causes a TypeError -->dimensions[0] = 250
# A tuple with one element my_t = (3,) the comma is needed

# Looping through all values in a tuple
# for dimension in dimensions:
# 	print(dimension)

#Writing over a Tuple
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)