# 任意字典
def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


profile = build_profile(first_name='John', last_name='Doe', email='test@email.com')
print(profile)


'''
 模块换调用
 from module name import function name 或者多个function，或者import *导入所有
 module name.function_name()
 别名
 from module_name import function_name as fn
'''