'''
This is a code for:-
- ABSTRACT CLASS
- ABSTRACT METHOD (they are just declared, but their definition is always within the sub-class)
'''

from abc import ABC, abstractmethod             # the abc is acronym for:- Abstract Base Class (this is importing)


'''
To make a class abstract, we do this:-

class <className>(ABC):

    @abstractmethod
    def <functionName>(self):
'''

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
class Car(Vehicle):
    def go(self):                               # this is the over-riding method
        print("The Car is GOING")
class Bike(Vehicle):
    def go(self):                               # this is another over-riding method
        print("The Bike is GOING")


# making the objects of the different classes

# vehicle = Vehicle()
''' IF YOU MAKE OBJECT OF VEHICLE, THERE WOULD BE A RUNNING ERROR AS IT IS ABSTRACT CLASS '''
car = Car()
bikes = Bike()

# vehicle.go()                                    vehicle's function
car.go()                                        # car's function
bikes.go()                                      # bike's function

# in short, if some class is extending an abstract class, or its abstract method, then it MUST have the function definition for the abstract method
