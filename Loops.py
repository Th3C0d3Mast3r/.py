# this is the file that contains different loops like:-
# for loops
# while loops
# do-while loops


import time

name=""
while len(name)==0:
    name=input("Enter Your Name: ")             # this will be looped until someone types the name


for i in range(10):                             # unlike java, this isn't:-  for(int i=0; i<10; i++)
    print(i)


for j in range(50, 100):                        # this is like:-  for(int j=50; j<100; j++)
    print(j)

# the for loop works in python as:-     for i in range(<start>, <end-1>, <increment by>)
print("NEW LOOP FROM 10 TO 39 WITH JUMPS OF 3")
for k in range(10, 40, 3):
    print(k)

# we can even loop for strings
print("Looping through the new name")
newName="Hello this is a Looping in String"
for i1 in newName:
    print(i1)                                   # the printing in loops is pre println form

print("\n\n\n\n\n")
# we import the time module here for this execution
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)                               # this is same is thread sleep and all that we knew in Java
print("HAPPY NEW YEAR")

rows=int(input("Enter the Number of Rows: "))
columns=int(input("Enter the Number of Columns: "))

for i in range(rows):                           # example of nested loops
    for j in range(columns):
        print("$", end="")                      # 
    print()                                     # this is for that orientation and all

'''
NOW WE LOOK AT THE LOOP CONTROL STATEMENTS:
They are mainly 3:-
- break
- continue
- pass
These are the basic ones and I won't be explaining them as their use remains the same, as in Java
'''

for i in range(1, 21):                          # pass is like, let go of it-but continue with the next one
    if(i==13):
        pass
    else:
        print(i)
