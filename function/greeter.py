def greet_user():
    print("Hello user")

greet_user()

# 这个地方原则上不是重载，而是根据定义顺序，后定义的函数覆盖前面的函数
def greet_user(username):
    print("Hello " + username)

greet_user("john")


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("What is your name?")
    print("Enter 'q' to quit")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    # 函数内触发调用
    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)

print("Thank you for playing!")