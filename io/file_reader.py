# 工程的包下，file文件夹可以使用相对路径
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    readlines = file_object.readlines()
for line in readlines:
    print(line.rstrip())


with open(filename) as file_object:
    readlines = file_object.readlines()
pi_string = ''
for line in readlines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))