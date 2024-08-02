# the index operator gives us access to Sequence element (be it String, tuples, lists)
name="firstname lastname"

if (name[1].islower()):
    name=name.capitalize()
print(name)

firs=name[:name.index(" ")].upper()                # Observe carefully-I got the space ka index via the function
print(firs)                                         # and the variable firs is not all caps

las=name[name.index(" ")+1:].upper()
print(las)

# in short, a string, list or tuple followed by [] would lead to choosing the characters at that index value