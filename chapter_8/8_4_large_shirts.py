def make_shirt(size = 'large',text = 'I Love Python!'):
	print(f"\nYour {text.title()} shirt in size {size} has shipped!")

make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'small', text = 'JavaScript is cool too!')