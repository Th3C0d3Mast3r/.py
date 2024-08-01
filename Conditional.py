# this is a file for all the conditional statements- if/elif/else

age=int(input("What is your age: "))
if(age>18):
    print("ADULT")
    print("SECOND LINE OF ADULT")
elif(age>60):
    print("SENIOR BOI")
elif(age>105):
    print("GOD LEVEL")
else:
    print("KIDS")

# a random if-elif-else block (these are th conditional statements that you can understand and easily use)

# We know head on to see conditional OPRTATORS

temp=float(input("What is the TEMPERATURE around: "))

if(temp>=0 and temp<=30):                       # the && of Java is 'and' in Python
    print("IT IS A MODERATE TEMPERATURE")
elif(temp<0 or temp>30):                        # the || of java is 'or' in Python
    print("ITS A BAD WEATHER OUTSIDE!")
elif(not(temp>0 and temp<50)):                  # the ! of Java is 'not' in Python
    print("HELICOPTER-HELICOPTER")
else:
    print("SIKE")