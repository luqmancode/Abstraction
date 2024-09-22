"""Abstract properties can also have setters, ensuring that subclasses implement both the getter and setter methods."""
from abc import ABC, abstractproperty, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @area.setter
    @abstractmethod
    def area(self, new_area):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @property
    def area(self):
        return self.length * self.breadth 
    
    @area.setter
    def area(self, new_area):
        raise NotImplementedError("Area could not able to set")
    
rectangle = Rectangle(3, 4)
print(rectangle.area)
rectangle.area = 500
print(rectangle.area)