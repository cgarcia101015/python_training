current_users = ['ally997', 'Garcia123', 'd.tomas', 'freddyPeppers01', 'Dave8832']

new_users = ['caro343', 'cyn.s998', 'garcia123', 'nyc8893', 'freddypeppers01']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(f"You need to enter a new username, {new_user} is not available.")
	else:
		print(f"The username {new_user} is available.")