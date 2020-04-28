from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

# Abstract class can only be inherited,objects can not be created.

class Square(Shape):
    side = 4
    def area(self):
        print("Area of square: ", self.side * self.side)

class Rectangle(Square):
    length = 4
    width = 5
    def area(self):
        print("Area of square: ", self.length * self.width)

sq = Square()
rt = Rectangle()
sq.area()
rt.area()
