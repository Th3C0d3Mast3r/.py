# a way to create new list using less syntax
# this is something that is for CODE REDUCTION and OPTIMIZATION over learning something essential or so

'''
squares=[]                      // creating an empty list
for i in range (1,11):
    squares.append(i*i)         // appending the squares into the list
print(squares)                  // printing the final list
'''
#the same above can be done in less code as follows:-

squares=[i*i for i in range (1, 11)]
print(squares)

# thus the syntax goes something like this:-
# <list_name> = [<expression> for <item> in <iterable>]
# <list_name> = [<expression> if/else for <item> in <iterable>]