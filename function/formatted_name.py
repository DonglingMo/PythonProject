def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    # 返回值
    return full_name.title()
print(formatted_name("john", "smith"))

# 定义可选参数
def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
print(formatted_name("john", "smith"))
print(formatted_name("john", "smith", "lee"))