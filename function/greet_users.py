def greet_users(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)