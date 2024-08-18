# This is something new to Python as well
# This assigns the value to the variables as a part of larger expression
# looks something like this -->    :=

'''
Suppose we wish to do this in python in one line; then we can use walrus:-

happy=True
print(happy)

'''

# thus, writing the above in a single line using walrus is as:-
print(happy:=True)

foods=list()
while True:
    food=input("What Food Do you Like to Have: ")
    if(food=="quit" or food=="exit" or food=="leave" or food=="terminate"):
        break
    foods.append(food)

print(foods)

''' TO WRITE THE ABOVE CODE IN SMALL LINES, WE DO THIS '''

'''
foods=list()
while food:=input("ENTER THE FOOD YOU WANT: ") != "quit":
    foods.append(food)

print(foods)
'''

# the problem is-what goes in the list is boolean value of True or False