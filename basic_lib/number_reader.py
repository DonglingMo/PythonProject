import json

filename = 'numbers.json'
with open(filename) as json_file:
    data = json.load(json_file)
print(data)