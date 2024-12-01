import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('Enter your name: ')
    filename = 'username.json'
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    # 在非import模式注意函数需要严格按照定义顺序声明
    username = get_stored_username()
    if username:
        print(f'Hello, {username}!')
    else:
        username = get_new_username()
        print(f"Welcome, {username}!")

greet_user()

