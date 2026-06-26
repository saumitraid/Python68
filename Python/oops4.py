# Single level inheritance
class Animal:
    def eat(self):
        print("Eating........")

class Dog(Animal):
    def bark(self):
        print('Barking.......')


ob=Dog()
ob.eat()
ob.bark()