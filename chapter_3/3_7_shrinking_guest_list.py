guest_list = ['Anthony Bourdain', 'Dave Chapplle', 'Joe Rogan']
print(f"Hi {guest_list[0]} would you like to join us for dinner?")

print(f"Hi {guest_list[1]} would you like to join us for dinner?")
print(f"Hi {guest_list[2]} would you like to join us for dinner?")

not_coming = guest_list.pop()
print(not_coming)
coming = guest_list.append('Barack Obama')
print(f"Hi {guest_list[0]} would you like to join us for dinner?")
print(f"Hi {guest_list[1]} would you like to join us for dinner?")
print(f"Hi {guest_list[2]} would you like to join us for dinner?")

guest_list.insert(0, 'Chris Rock')
guest_list.insert(2, 'The Rock')
guest_list.append('Jim Carey')
print(guest_list)
print(f"Hi {guest_list[0]} would you like to join us for dinner?")
print(f"Hi {guest_list[1]} would you like to join us for dinner?")
print(f"Hi {guest_list[2]} would you like to join us for dinner?")
print(f"Hi {guest_list[3]} would you like to join us for dinner?")
print(f"Hi {guest_list[4]} would you like to join us for dinner?")
print(f"Hi {guest_list[5]} would you like to join us for dinner?")
print("We have found a bigger table!")

print("Sorry, unfortunetly I can now only invite two people to dinner!")
removed_guest = guest_list.pop()
print(f"Sorry I can't invite you to dinner {removed_guest}!")
removed_guest = guest_list.pop()
print(f"Sorry I can't invite you to dinner {removed_guest}!")
removed_guest = guest_list.pop()
print(f"Sorry I can't invite you to dinner {removed_guest}!")
removed_guest = guest_list.pop()
print(f"Sorry I can't invite you to dinner {removed_guest}!")
print(f"Hi {guest_list[0]}, you're still invited to the dinner.")
print(f"Hi {guest_list[1]}, you're still invited to the dinner.")
del guest_list[0]
del guest_list[0]
print(guest_list)

