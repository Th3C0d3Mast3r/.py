# This is where we start the object-oriented programming in Python
# This serves as the foundation for good programming practices
# Prior to this, we explored data structures in Python
# Now, let's look at the class definition and its usage

class Car:  # Renamed to singular form
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def drive(self):
        print("Self-driving car activated!")

    def stop(self):
        print("Car stopped.")

# If the class is in a separate file, uncomment the following line
'''     from OOPS import Car        '''

# Creating an instance of the Car class
car1 = Car("Chevy", "Latest", "Black")
print(car1.make)  # Should print: Chevy  

car1.drive()
car1.stop()

car2=Car("Buggati", "Chiron", "Blue")
print("\n\n"+car2.make+" "+car2.model)