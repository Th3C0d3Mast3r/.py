# this is acted on the first two values, and goes on until we are left till the last element.
# reduce also has two parameters

import functools                                # we have to import this so as to use reduce()

letters=["H", "E", "L", "L", "O"]
togethers=lambda x,y:x+y
word=functools.reduce(togethers,letters)

print(word)                                     # this would print the word concatenated together.

factorial=[5,4,3,2,1]
facts=lambda x,y:x*y
facto=functools.reduce(facts, factorial)
print("the factorial that we got is:- ", facto)

# this is a rather good function when we need to use all the things in the list for some work to be done