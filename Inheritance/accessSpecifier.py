# Public attribute
class Car:
    numberOfWheels = 4
    _color = 'black'
    __yearOfManufacture = 2017 # internally _Car_yearOfManufacture
class BMW(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)

car = Car()
print("Public: ", car.numberOfWheels)
bmw = BMW()
print("Private attribute: ", car.__yearOfManufacture)
