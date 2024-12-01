from syntax.toppings import topping

pizza = {
    'crust': 'think',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(pizza['crust'])
for topping in pizza['toppings']:
    print(topping)