# we usually pass variables as the parameters
# here we will be passing OBJECTS in FUNCTION PARAMETERS

class Car:
    color="Blue"
    brand="Lambo"

def changeColor(car, color):
    car.color=color

car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()

changeColor(car1, "Red")
changeColor(car2, "Orange")
changeColor(car3, "Gold")

print("Car 1's color:- ",car1.color)
print("Car 2's color:- ",car2.color)
print("Car 3's color:- ",car3.color)
print("Car 4's color:- ",car4.color)        # the default color

# since python doesn't need the datatype specifications and all, this becomes relatively easy 