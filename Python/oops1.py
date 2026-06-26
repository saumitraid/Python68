class Person:
    name="Rahul"  #Data member
    def talk(self):  #Member function/method
        print("Person can talk")

# Creating object
obj=Person()
print(obj.name)
obj.talk()


obj1=Person()
obj1.name="Amit"
print(obj1.name)
obj1.talk()

