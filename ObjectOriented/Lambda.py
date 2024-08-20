# lambda functions in python are shortcut for such functions that you require for short time and would eventually throw away
# the syntax is:-  lambda <parameters>:<expression>

'''
def intoTwo(x):
    return x*2
'''

timesTwo=lambda x:x*2
print(timesTwo(10))

fullNmame=lambda firstname, lastname:firstname+" "+lastname
print(fullNmame("COMPLETE", "NAME"))

# this is the base way for labmda functions