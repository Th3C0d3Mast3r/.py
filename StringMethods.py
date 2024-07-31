# The following are some of the in-built functions of Python

name = "person name"
stringLength = len(name)                                    # the function is as: len(<stringName>)
print("Length of name is:- ",stringLength)                  # this will even count whitespace as a character

firstIndex = name.find("n")                                 # index value of the first occurrence of 'n'
print("The First-Index of letter 'n' is:- ", firstIndex)

print("name after capitalization:- "+name.capitalize())     # Only the First Letter is capitalized

nameAllCaps=name.upper()                                    # ALL UPPERCASE
print(nameAllCaps)

nameAllSmall=name.lower()                                   # all lowercase
print(nameAllSmall)

print(name.isdigit())                                       # returns boolean if string is digit or no
# Note that the above works only for the case where String has digits or no- not int data-type

print(name.isalpha())                                       # returns boolean if string is pure alphabets

# Added to that, Python even has the function where one can see the number of letter repition in String

print("Number of 'n' in name:- ", name.count("n"))

newName=name.replace("n", "d")                              # Replaces 'n' by 'd'
print(newName)

# this is not a function but a cool feature
print(nameAllCaps*5)                                        # Prints the string 5x

# THERE ARE MORE FUNCTIONS. IF YOU ARE ON VSCODE OR PYCHARM, YOU CA EXPLORE THEM VIA-
# USE THE VARIABLE, AND AFTER THAT, TYPE A '.'
# E.g. name.  and then you would see list of functions applicable