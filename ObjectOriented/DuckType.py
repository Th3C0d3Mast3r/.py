# this is a rather new concept that we are dealing with.
# so something new to learn

class Duck:
    def walk(self):
        print("DUCK WALKS")
    def talk(self):
        print("QUACKING")

class Chicken:
    def walk(self):
        print("CHICKEN WALKING")
    def talk(self):
        print("CLUCKING")

# obsereve that both of them have the same method name-but prints something different

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("CAUGHT")

duck = Duck()
chick = Chicken()
person = Person()

person.catch(duck)                          # this is equal to passing an object
# NOTES:- Even if I were to pass the chicken object, it would still work because both of them had the same functions
print("\n")
person.catch(chick)

'''
THUS, DUCK-TYPE IS SOMETHING THAT IS PROMINENT FEATURE
IN THIS, THE CLASS AND ITS OBJECT IS NOT GIVEN ANY SORT OF IMPORTANCE.
RATHER, THE FUNCTIONS OF THE CLASS ARE WHAT MAKE IT MORE WORTH IT!
'''