cars = ['bmw', 'audi', 'toyota', 'subaru']
# 永久改变的排序
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# 临时排序
print(sorted(cars))
print(cars)

# 长度
print(len(cars))