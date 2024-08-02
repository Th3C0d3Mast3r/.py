# NOW THIS SEEMS REALLY DIFFERENT
# TUPLES IS SOMETHNIG, IG, NOT IN JAVA

'''
as per the definition of Tuples, tuples are-
- Collection of SAME LINKED DATA
- They are SEQUENCE SENSITIVE
- They are UNCHANGEABLE
'''

tuple1=("guestName", 15, "male", "undergraduate")                   # this has name, age, gender and ed-stat
reps=tuple1.count("guestName")                                      # number of time the data is seen in the tuple
print(reps)

for x in tuple1:
    print(x)