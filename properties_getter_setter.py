"""Properties allow you to define getter, setter, and deleter methods for class attributes, providing a way to control access to the attributes."""

from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            print("Radius could not be negative")
        self.__radius = new_radius

    @property
    def area(self):
        return 2 * pi * self.__radius
    
circle = Circle(5)
print(circle.radius)
print(circle.area)
circle.radius = 10
print(circle.area)