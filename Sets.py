# set is a collection which is unindexed and unordered 

objectsAround={"lamp", "pen", "phone"}
for x in objectsAround:
    print(x)

# the thing is, they are randomly printed
# thus, it is faster than LISTS and dont ALL DUPLICATES

objectsAround.add("lamp")
objectsAround.add("Mouse")
print(objectsAround)                                        # You would observe lamp comes once only

utensil={"spoon", "fork", "plate", "chopstiks"}

# in order to add one set into another, we do this:-
objectsAround.update(utensil)
print(objectsAround)

# this sets is same as the Mathematical Sets-we can add them, and even have union and all

newSet=objectsAround.union(utensil)
print("This is the kind of UNIVERSAL SET for the above two sets:- ",newSet)

print(objectsAround.difference(newSet))                     # If you observe, this would be null set as I had updated objectsAround with utensils while new set is union of this
print(utensil.intersection(newSet))                         # Prints the data common to them

'''
Thus, here is the Quick Sum up of the COLLECTION OF DATATYPES WE HAVE IN PYTHON:-
1) LISTS:- Allows repetitive data and is ORDERED. For lists, use [ ]
2) TUPLES:- SEQUENCE SENSITIVE and UNCHANGEABLE data that is RELATED. For tuples, use ( )
3) SETS:- Same as the Mathematical Sets-no reps allowed, and RANDOM printing. For sets, use { }
'''