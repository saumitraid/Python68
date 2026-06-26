class Vehicle:
    color=""
    regNo=""
    brand=""
    # Paremeterize Constructor
    def __init__(self, color, regNo, brand):
        self.color=color
        self.regNo=regNo
        self.brand=brand

    def moveForward(self):
        return "Move forward"
    
    def moveBackward(self):
        print("Move backward")
    
    def getData(self):
        print("Brand:-",self.brand)
        print("Color:-", self.color)
        print("Registration Number:-", self.regNo)

v1=Vehicle("White", "WB12AA5048", "Maruti Suzuki")
v1.getData()
print(v1.moveForward())

# WAPP for factorial of a number using parameterize constructor and the
#  number is user input

