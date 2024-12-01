players = ['charles', 'martina', 'michael', 'florence', 'eli']
# index区间，左闭右开,切片
print(players[0:3])
print(players[1:4])


print(players[:4])
print(players[2:])
# 最后个元素
print(players[-3:])

# 遍历，数据处理更多采用切片
for player in players[:3]:
    print(player.title())