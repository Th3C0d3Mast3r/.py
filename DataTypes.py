# In Python, unlike Java, we do not use any DataType before the variable name
# It just starts (it is how it is)

firstName = "Razu"            # this is a String datatype
lastName = "Kazu"
age = 34                      # this is an integer datatype
bankBalance = 234567.3245     # this is a float datatype
billionaireStatus = False     # this is a boolean datatype (True/False with initial capital)

print("These are the Details of Person\n")
print("Name:", firstName + " " + lastName + "\nAge:", age, "\nBank Balance:", bankBalance)
print("Is the person Billionaire Yet:", billionaireStatus)

# Printing data types in the same sequence
print("\n\n")
print("Name:", type(firstName).__name__, type(lastName).__name__)
print("Age:", type(age).__name__)
print("Bank Balance:", type(bankBalance).__name__)
print("Is the person Billionaire Yet:", type(billionaireStatus).__name__)
