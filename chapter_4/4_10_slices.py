big_cats = ['lion', 'cougar', 'tiger', 'panther', 'lynx', 'cheetah', 'leopard', 'puma', 'jaguar']

for cat in big_cats:
	print(f"A {cat} would not make a great pet!")
print(f"Any of these animals could rip your face off!")

print("The first three items in the list are:")

for cat in big_cats[:3]:
	print(cat)


print("Three items from the middle of the list are:")

for cat in big_cats[3:6]:
	print(cat)

print("The last three items in the list are:")

for cat in big_cats[-3:]:
	print(cat)
