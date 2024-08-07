# this is the same as we have try-catch-finally thing in JAVA
# Called as Exception Handling

try:
    x=int(input("Enter the Numerator: "))
    y=int(input("Enter the Denominator: "))
    result=x/y
except ZeroDivisionError as e:                                      # this is SPECIFIC catch block equivalent
    print("Whoops! Can't Divide by Zero-Error Detected:",e)
except ValueError as e:
    print("Thats Not a CORRECT Division-Error Detected:",e)
except Exception as e:                                              # this is like catch(Exception e)
    print("Some Error Occured-Error Detected:",e)
else:
    print("The Answer for Division is: {}".format(result))
finally:
    print("WE ARE GONE NOW")                                        # same as 'finally' of Java