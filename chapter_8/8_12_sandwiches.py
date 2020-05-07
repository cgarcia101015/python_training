def make_sandwich(*items):
	"""Summarize the sandwich we are about to make."""
	for item in items:
		print("...adding " + item + " to your sandwich.")
	print("Your sandwich is ready")


make_sandwich('ham','american cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')