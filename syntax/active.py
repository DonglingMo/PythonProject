prompt = "\nTell me something, then press enter."
prompt += "\nEnter 'quit' to continue."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)