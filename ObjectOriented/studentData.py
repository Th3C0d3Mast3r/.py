# this is how you can use list of tuples in python
# rather tan creating a linked array based on the index number-as we do in java, this seems more convinient


def get_student_data():
    student_data = []  # Initialize an empty list to store student tuples

    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        
        if name.lower() == 'done':
            break  # Exit the loop if the user types 'done'
        
        course = input("Enter course: ")
        student_id = input("Enter student ID (integer): ")
        
        # Validate student ID
        while not student_id.isdigit():
            print("Invalid input for student ID. Please enter an integer.")
            student_id = input("Enter student ID (integer): ")

        student_id = int(student_id)  # Convert student ID to integer

        # Create a tuple and add it to the list
        student_tuple = (name, course, student_id)
        student_data.append(student_tuple)
        
        print(f"Added!")

    return student_data

# Call the function and store the result in a variable
students = get_student_data()

# Print the list of student data
print("Student Data:")
for student in students:
    print(student)
