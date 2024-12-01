def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name}.")
# 实际参数1.按位置定义，2.准确指定参数名称与位置无关，3.在函数形参中指定默认值
# 参数不匹配则报错
describe_pet(animal_type='dog', pet_name='cat')