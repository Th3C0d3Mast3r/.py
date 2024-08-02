# the following is the topic of lists
# lists refers to store multiple items in the same variable
# this is in short ARRAY of java

foodItem=["pizza", "dhokla", "paratha", "thepla"]
print(foodItem)
print("NOW PRINTING THEM VIA FOR LOOP and INDEX WISE")
for i in range(len(foodItem)):                                  #  same as:-   for(int i=0; i<foodItem.length; i++)
    print(foodItem[i])

# another way to do the above task is via this method-
print("ALTERNATE METHOD:-")
for i in foodItem:
    print(i)

'''
THERE ARE SEVERAL TYPES OF IN-BUILT FUNCTION IN PYTHON
FOR USING AND MANIPULATING ARRAYS (aka lists)
THE FOLLOWING CAN BE ACCESSED VIA TYPING-
<listName> .
if there is an IDE, then the list of functions is easily seen and used
'''

lengths=foodItem.count("pizza")
print("The number of reps of PIZZA is:", lengths)

foodItem.append("Vada Pav")                                     # the .append("") adds the value given at the end
foodItem.remove("pizza")                                        # the .remove("") removes the given if present in list
foodItem.pop()                                                  # the pop is the stack function and follows LIFO Logic

foodItem.insert(0, "Ras Malai")                                 # the .insert() adds the data at the nth index
print("this is the edited list now:-\n",foodItem)
foodItem.sort()
print("SORTED LIST IS:- ", foodItem)

# and to clear the whole list, we do-   foodItem.clear()