prompt = "\nPlease enter a city name:\n"
prompt += "\n(Enter 'q' to quit)"

while True:
    city = input(prompt)
    if city == 'q':
        break
    else:
        print(city)