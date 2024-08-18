# this is something similar to POINTERS in C
def hellos():
    print("HELLO FRIENDS")

hi=hellos                                               # hi holds the location to the function hellos()
print("PRINTING JUST:- hellos",hellos,"\n")
print("PRINTING JUST:- hi",hi,"\n")
hi()

# This is something that won't be used that much- but you know what they say
# Better to have some things up your sleeves