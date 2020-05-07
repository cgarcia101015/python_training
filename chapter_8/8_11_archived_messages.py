def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ['wattup', 'lol', 'wtf', 'yolo', 'wya', 'wth', 'smh']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)