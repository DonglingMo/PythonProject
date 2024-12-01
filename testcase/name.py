from testcase.name_function import get_formatted_name

print("Enter 'q' to quit")
while True:
    first = input("First name: \n")
    if first == 'q':
        break
    last = input("Last name: \n")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(formatted_name)