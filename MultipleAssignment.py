# This is for Multiple Assignment in Python is
# Allows us to addign multiple variables in a single go

'''
well, till now, we did this-
age= 45
name= "Lol Sike"
booleans= True
'''

# We can do the same via-
age, name, booleans=45, "Lol Sike", True
# note:- The order in the above is crucial. As it assigns as per corresponding variable
# It wont be anything wrong(as there is no datatype specification pre-hand)
# It just becomes a logical error in your code tho

print("Age:- ", age)
print("Name:- "+name)
print("Boolean Status:- ", booleans) 

# Now, for the case of two or more variables having same values, we do as we do in Maths
RajuAge=PanduAge=BabuAge=19

print("Raju's Age: ", RajuAge)
print("Pandu's Age: ", PanduAge)