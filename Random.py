import random

x=random.randint(1,6)                       # to generate a random integer in range of 1 to 6
print(x)

y=random.random()                           # to generate random floating point value
print(y)

mylist=["obj1", "obj2", "obj3", "obj4"]
print(random.choice(mylist))                # we random is the module, while choice is its function

# now we can even shuffle the list using the random module

cardDeck=[1,2,3,4,5,6,7,8,9,"Jack", "Queen", "King", "Ace"]
random.shuffle(cardDeck)

print(cardDeck)
# THERE ARE MORE FUNCTIONS OF random MODULE. See them via typing random. and list of functions are displayed