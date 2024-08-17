# I wont be telling what inheritance is and all that
# this will just show all the codes and all in Python

class Animal:
    alive=True
    
    def eat(self):
        print("ANIMAL IS EATING CHOMP-CHOMP")
    
    def sleep(self):
        print("THE ANIMAL SLEEPS")
    

class Rabbit(Animal):                            # this is equivalent to class Rabbit extends Animal
    pass

class Lion(Animal):
    pass

# creatng objects of each class here:-
rabbit = Rabbit()
lion = Lion()

rabbit.eat()                                    # although I havent written any method in rabbit, it still has alive()

'''
THIS BELOW IS FOR MULTI-LEVEL INHERITANCE (derived class inherits another Derived class)

Main Class <-- Middle Class <-- Bottom Class
'''
# I hope that you know the base difference between MULTIPLE and MULTI-LEVEL Inheritance

class Organism:                                 # Organism is the main Parent Class
    isalive=True
    location="Earth"

class ABC(Organism):                            # ABC extends its Parent Class Organism
    def eat(self):
        print("EATING CHOMP CHOMP")
    
class XYZ(ABC):                                # XYZ extends a base class, which is Parent to XYZ, but Child to Organism
    def habits(self):
        print("I AM A DANSOR!")

xyz = XYZ()                                     # object creation
abc = ABC()                                     # object creating

print("\n\n\n")
xyz.habits()                                    # habits is a function of XYZ classs
xyz.eat()                                       # but eat() is a function of ABC
print("The Animal lives on "+xyz.location)      # and location is a data-member of grandpa of XYZ; i.e., Organism
