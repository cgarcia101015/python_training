"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('aprilla')
print(motorcycles)

motorcycles = []
motorcycles.append('harley davidson')
motorcycles.append('indian')
motorcycles.append('triumph')
print(motorcycles)

motorcycles.insert(0, 'victory')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)
#Removing an Item Using the pop() Method
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop()
print(f"The last mortorcycle I owned was a {last_owned.title()}.")

#Popping items from any Position in a List
motorcycles = ['honda','yamaha','suzuki']

first_owned = motorcycles.pop(0)
print(f"The first mortorcycle I owned was a {first_owned.title()}.")
#Removing an item by Value
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
"""
#Avoiding Index Errors When Working with Lists
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles[-1])

