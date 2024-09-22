"""Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This is a form of runtime polymorphism."""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self): # method overriding
        print(f"{self.name} makes hokkkk!!!")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} makes Woofff")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} makes Meowwww")

dinosour = Animal('Flexy', 5)
dinosour.sound()

dog = Dog('Huskey', 4)
dog.sound()

cat = Cat('Mera', 3)
cat.sound()