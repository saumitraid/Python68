class Vehicle:
    color=""
    regNo=""
    brand=""
    # Non Paremeterize Constructor
    def __init__(self):
        print("This is a Constructor")

    def moveForward(self):
        print("Move forward")
    
    def moveBackward(self):
        print("Move backward")
    
    def stop(self):
        print("Stop")

v1=Vehicle()
# v1.brand="BMW"
# v1.regNo="WB20AB1024"
# v1.color="White"
# print(v1.brand, v1.regNo, v1.color)
# v1.moveForward()
# v1.moveBackward()
# v1.stop()
