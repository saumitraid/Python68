# Multi level inheritance
class Animal:
    def eat(self):
        print("Eating........")

class Dog(Animal):
    def bark(self):
        print('Barking.......')

class Puppies(Dog):
    def cry(self):
        print("Crying.......")

    # Method overriding 
    def eat(self):
        print("Drink milk.....")

obj=Puppies()
obj.eat()
obj.bark()
obj.cry()