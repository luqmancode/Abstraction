"""Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is often achieved through method overriding and interfaces."""
import math 

class Shape: # Not interface but method overriding
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth 
    
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 2 * math.pi * self.__radius
    
rectangle = Rectangle(3, 4)
circle = Circle(5)

shapes = [rectangle, circle]

for shape in shapes:
    print(shape.area()) # interface