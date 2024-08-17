# Well, this seems something new-something not there in Java as such
# Don't worry-its just a fancy name
# Method chaining in short refers to calling multiple methods sequentially 

class Car:
    def starts(self):
        print("THE ENGINE STARTS")
        return self                             # the return self is what plays the main thing in chainning

    def drive(self):
        print("THE CAR DRIVES")
        return self

    def brake(self):
        print("BRAKES HIT")
        return self
    
    def turnOff(self):
        print("THE ENGINE IS SWITCHED OFF")
        return self
    
car = Car()
car.starts().drive().brake()                    # the sequence is:-  starts() -> drive() -> brake()
car.turnOff()