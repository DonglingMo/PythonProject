requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('This topping is not an anchovies.')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

if requested_toppings:
    for topping in requested_toppings:
        print(topping)
else:
    print('No toppings')