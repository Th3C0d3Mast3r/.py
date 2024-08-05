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

'''RETURN STATEMENT IN THE FUNCTIONS'''
# IN JAVA, THE void or boolean IS THE RETURN TYPE
# WHICH MEANS, THE RETURN TYPE OF THAT FUNCTION WOULD BE OF nothing or boolean ACCORDINGLY

x=int(input("ENTER THE FIRST INTEGER:- "))
y=int(input("ENTER THE SECOND INTEGER:- "))

def multi(int1, int2):
    result=int1*int2                                            # WE NEED NOT MAKE A VARIABLE TO STORE IT-I JUST DID FOR SAKE OF UNDERSTANDING
    return result

results=multi(x,y)
print("\n\nTHEIR MULTIPLICATION RESULT IS:- ",results)



# some more of python functions and their property

def greeting(firstN, middleN, lastN):
    print("GREETINGS!\nYou must be "+firstN+" "+middleN+" "+lastN)

greeting("firstName", "middleName", "lastName")                 # THEY ARE ORDERED PARAMETER PASSING
print("\n")
greeting(firstN="Suresh", lastN="Sharma", middleN="Mohit")      # THUS, THEY NEED NOT BE ORDERED, BUT ARE ASSIGNED PROPERLY


# NESTED FUNCTION CALLS IN PYTHON

'''
nums=input("ENTER A NON-NEGATIVE INTEGRAL NUMBER:- ")
nums=float(nums)
nums=abs(nums)
nums=round(nums)
print("YOU ENTERED:- ", nums)
'''
# the above can be written as:-
print("YOU ENTERED:- ",round(abs(float(input("ENTER A NON-NEGATIVE INTEGRAL NUMBER:- ")))))


# SCOPE OF VARIABLE (this is in short, local, instance , global, static and all those variable types as in Java)
# not writing much on this as it is something easy and no need for any code for that
# ORDER OF PREFERENCE-   LEGB:- Local --> Enclosing --> Global --> Built-In

# *args formatting in Python

# so, the function def sums(num1, num2) works for only two parameters
# but what if someone enters more than two
# for such cases, we use the tuples parameter
# using *args creates a tuple named args-and then, we can iterate through that. 
# RECALL:- Lists=[ ],  Sets={ },  Tuples=( ) and Dictionaries/HashMaps={ : }

def sums(*args):
    sum=0
    for i in args:
        sum+=i
    
    return sum

print(sums(2,3,4,5,6,77))                                       # The Sum of this should be 97


# just as we had *args, there is something even called as **kwargs
# well, *aegs made all in TUPLES
# while **kwargs is what makes the HASH MAP(or say DICTIONARY)

def hello(**kwargs):
    print("Hello", end=" ")                                     # as said before too, end="" prevent new line shift
    for key,value in kwargs.items():                            # the key,value is for the hashmap accessing
        print(value, end=" ")


hello(title="Mr", name="Anderson", Middle="Michael", last="Bois")
