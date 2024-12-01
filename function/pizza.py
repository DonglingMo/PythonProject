# 空元组，任意数量参数
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni', 'mushroom')

def make_pizza(size, *toppings):
    print(f'making {size}')
    for topping in toppings:
        print(topping)
make_pizza(12, 'pepperoni', 'mushroom')
make_pizza(16, 'pepperoni')