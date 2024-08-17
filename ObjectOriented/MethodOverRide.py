# this is a program for METHOD OVER-RIDING
# Like, if there is a confilct between two functions that have the same name, then the function in closer one is given priority
# say- class ABC is base class and class XYZ is sub-class
# Now, both have a function called doSomething().
# So, when the xyz.doSomething() is called, it will run the function under XYZ over ABC
# this is the base thing behind function/Method Overriding

class Animal():                                             # Animal is the base class
    def someFunction(self):
        print("THIS IS THE FUNCTION IN MAIN CLASS")

class Human(Animal):                                        # Human extends the class Animal
    def someFunction(self):
        print("THIS IS FUNCTION OF HUMAN NOT ANIMAL")

humans = Human()
humans.someFunction()                                       # NOTES:- Both have same function name, but this triggers in Human
