class Dog:
    """ 构造函数 self指向类本身 """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} is now rolling over')