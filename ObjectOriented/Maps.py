# the map() is a function in Python
# it is applicable with two present parameters:-
# map(function, iterable)

store=[("shirt", 20.0),                             # this is a list of tuples
       ("pants", 25.0),
       ("jacket", 30.0)]
toEuros=lambda data:(data[0], data[1]*0.0108)

store_euros=list(map(toEuros, store))

print(store_euros)                                  # this is the store with the values in Euros converted from INR

'''SOME MORE ABOUT THE MAP FUNCTION'''
