class Shape:
    def area(self):
        print("Area method not implemented in base class.")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

square = Square(5)
rectangle = Rectangle(4, 6)

print("Area of Square:", square.area())
print("Area of Rectangle:", rectangle.area())