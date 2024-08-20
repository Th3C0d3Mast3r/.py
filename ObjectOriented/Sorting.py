# NOTES:- The .sort() function works ONLY for LISTS and not for Tuples or Sets

students=["first", "second", "third", "fourth"] # this is a list
# to sort using the in-built function, all we do is:-
students.sort()
print(students)

# for a reversed sorting, we do this:-
students.sort(reverse=True)
print(students)

# now we deal with list of tuples

student=[("ABC", "F", 60),
         ("DEF", "A", 90),
         ("XYZ", "B", 82),
         ("AAA", "D", 70),
         ("AXE", "Z", 101)]

student.sort()  # this got sorted on the basis of the alphabet in the first column-aka, the name
print(student)

# sorting them based on their grades, we do:-
grade=lambda grades:grades[1]       # when we put grades[1], we meant the data in the sets index location 1
                                    # we could do the same for sorting on marks by putting makrs[2] for index 2
student.sort(key=grade)
print(student)