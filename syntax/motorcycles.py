motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 列表不是不可变的
motorcycles[0] = 'ducati'
print(motorcycles)
# 末尾添加
motorcycles.append('ducati2')
print(motorcycles)

# 初始化
motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(f'motorcycles2: {motorcycles2}')

# 指定位置插入
motorcycles.insert(0, '1ducati')
print(motorcycles)

# 删除元素
del motorcycles[0]
print(motorcycles)

# FILO stack
pop = motorcycles2.pop()
print(motorcycles2)
print(pop)

# 指定位置弹出
motorcycles_pop = motorcycles.pop(0)
print(f'motorcycles_pop: {motorcycles_pop}')

# 按值删除
motorcycles3 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles3)
motorcycles3.remove('ducati')
print(motorcycles3)

# motorcycles3.remove('a') panic!
# print(motorcycles3)

