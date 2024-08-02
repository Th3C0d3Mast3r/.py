# this is the file that contains different loops like:-
# for loops
# while loops
# do-while loops

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