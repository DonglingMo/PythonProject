from oop.Car import Car, ElectricCar

my_new_car = Car('subaru', 'outback', 2018)
print(my_new_car.get_descriptive_name())
my_new_car.increase_odometer(100)
my_new_car.read_odometer()

my_new_car.increase_odometer(50)
my_new_car.read_odometer()
print()
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()