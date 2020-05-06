def show_messages(texts):
	"""Prints all the items in a list"""
	for text in texts:
		print(text)

def send_messages(texts):
	while text_messages:
		new_list = texts.pop()
		print(new_list)
		sent_messages.append(new_list)


text_messages = ['wattup', 'lol', 'wtf', 'yolo', 'wya', 'wth', 'smh']
sent_messages = []
send_messages(text_messages)

print(f"text_messages: {text_messages}")
print(f"sent_messages: {sent_messages}")