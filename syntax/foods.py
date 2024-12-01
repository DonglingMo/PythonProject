my_foods = ['pizza', 'falafel', 'carrot cake']
# 有列表复制为切片, 切片为副本，所以修改并不会互相影响
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# 指向同一个列表
friend_foods2 = my_foods
my_foods.append('cannoli2')
friend_foods2.append('ice cream2')
print(my_foods)
print(friend_foods2)

# 字符串处理 [::-1]
# 元素遍历，部分替换，清空
# 算法操作