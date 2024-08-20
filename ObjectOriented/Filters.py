# this is a filter function in python
# just as we have filters in excel and all, this is the same thing in python
# works as:- filter(function, iterable)    IN MANY CASES, ITERABLE IS THE LIST WHICH WE WISH TO FILTER DATA FROM

friends=[
    ("rachel", 19),("raju", 20), ("pandey", 15), ("brandon", 22), ("austin", 33), ("jose", 12), ("brandi", 17)
]

# now I want to filter the ones who can go out and drink in a bar (DRINKING IS INJURIOUS TO HEALTH AND MAY CAUSE FATAL PROBLEMS)

ageRestrict=lambda data:data[1] >= 18                   # as the 1st index is the age

drinkableList=list(filter(ageRestrict, friends))

print(drinkableList)                                    # list of ones who can legally drink (NOT RECOMMENDED)