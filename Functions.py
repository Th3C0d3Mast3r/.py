# Functions/Methods play an important role in any language
# They are the small blocks in a code that actually enable us to write a robust code
# Thus, pay HARD AND WELL ATTENTION WHILE LEARNING FUNCTIONS

'''
IN JAVA WE HAVE SEEN FUNCTIONS ARE SOMETHING LIKE THIS:-

private static void newFunction()
{
}

public boolean isTrueFunction(String response)
{
}
''' 

def functions():                                            # def is the thing that makes it function and () too
    print("INSIDE THE FUNCTION")                            # THE INDENTED THING MAKES IT INSIDE THE FUNCTION BLOCK

functions()                                                 # CALLING THE FUNCTION


name=input("ENTER YOUR NAME:- ")
# secondFn(name)                                            THIS WONT WORK BECAUSE THIS FEATURE IS LIKE C LANGUAGE

def secondFn(parameter1):
    print("This is the parameter passed:- "+parameter1)

secondFn(name)

integ=int(input("ENTER THE INTEGER:- "))
def thirdFn(integerVal):
    print("THIS IS THE INTEGER VALUE PASSED:- ", integerVal)
thirdFn(integ)