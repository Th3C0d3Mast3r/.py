# the string method .format() is for string values
# it allows the user to use and display the string in various formats

# supposedly, we have somehting like this:-
animal="horse"
object="fence"

print("The "+animal+" jumped over the "+object)

# I can write the same thing in this manner as well:-

print("The {} jumped over the {}".format(animal, object))       # THE {} ACTS AS A PLACE HOLDER IN PYTHON PRINT STATEMENT
# but these place holders(format field) are SEQUENTIALS
# to make it free, we do this


print("The {0} jumped over the {2} while {1}".format(animal, "running", object))

# to make padding to our text and all, we do this:-
print("The {:10} jumped over the {:^10} while running around".format(animal, object))

print("The {0:>10} jumped over the {2:^10} while {1:<10}".format(animal, "running", object))

# thus, the {<indexvalue> : <spacing amount>} format works like this with 
# ^  = center align
# <  = left align
# >  = right align


num=12348

print("The Number is {}".format(num))                           # Base print number
print("The Number is {:b}".format(num))                         # number in binary
print("The Number is {:o}".format(num))                         # number in octal
print("The Number is {:x}".format(num))                         # number in hexadecimal
print("The Number is {:E}".format(num))                         # number in scientific notations

