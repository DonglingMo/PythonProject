responses = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to pull? ")

    responses[name] = response

    repeat = input("Would you like to pull again?(yes/no) ")
    if repeat == "no":
        polling_active = False

for name, response in responses.items():
    print(f"{name}: {response}")