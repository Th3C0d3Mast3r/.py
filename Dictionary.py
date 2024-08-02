# this is a file that deals with Dictionaries in Python
# Dictionary- A changeable unordered collection of Unique key:value pairs
# this is assumingly similar to that of java HashMap

capitals={"INDIA":"NEW DELHI", "USA":"WASHINGTON DC", "AUSTRALIA":"CANBERA"}

print(capitals["AUSTRALIA"])                                    # this would give the value associated with australia

# print(capitals["NEW DELHI"]) this will throw error as this is like a ray and not line
# as in, it is pointing FROM country TO the capital. The vice versa aint true                                
# thus we use the .get() function to avoid such errors of non existent

print(capitals.get("INDIA"))                                    # this exists
print(capitals.get("GERMANY"))                                  # this doesn't exist

print(capitals.keys())
print(capitals.values())

# to add more hashmaps, we use the .update() method
capitals.update({"MEXICO":"MEXICO CITY"})
capitals.update({"USA":"WASHINGTON"})                           # with the same, you can change the existing pair
print(capitals.get("USA"))

print(capitals.items())                                         # this prints all the hash pairs
print(capitals.get("mexico"))
print(capitals.get("MEXICO"))                                   # this is case sensitive things

# Since the .update() added in the end, thus, this is also stack format based
# Thus, Dictionaries also have the feature of .pop() and .clear()

'''
A QUICK RECAP
LISTS:- [ ]
TUPLES:- ( )
SETS:- { }
DICITONARIES:- { : }
'''