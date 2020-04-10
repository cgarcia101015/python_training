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
