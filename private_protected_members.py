"""Private and protected members are used to restrict access to certain attributes or methods within a class. Private members are not accessible outside the class, while protected members are accessible within the class and its subclasses."""

class Person:
    def __init__(self, name, age):
        self._name = name  # Protected
        self.__age = age  # Private

    def get_age(self):
        return self.__age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age


p1 = Person('Warner', 45)
# print(p1.name) # AttributeError: 'Person' object has no attribute 'name'. Did you mean: '_name'?
print(p1._name)
print("Methods to get age: ", p1.get_age())
p1.age = 5
print("Using getter to get age: ", p1.age)
p1.__age = 60
print("Using Private Variable to get age: ", p1.__age)