class Encapsulation:
    name="Rohan"  #public
    _email='rohangmail.com' #protected
    __mobile="789654130"    #Private

ob=Encapsulation()
print(ob.name)
print(ob._email)
print(ob.__mobile)
