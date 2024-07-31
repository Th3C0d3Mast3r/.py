# this is type casting in Python
# we convert one data type in another

integerType=1234
floatType=234.456
stringType="this is a string"

floatToInt=int(floatType)               # we convert the float to integer type
intToFloat=float(integerType)           # we convert the integer to float type

print("We see this ",floatType," change to ",floatToInt," with new type: ",type(floatToInt))
print("We see this ",integerType," change to ",intToFloat," with new type: ",type(intToFloat))

# in java, for String to Int, we do:-  int numStr=Integer.parseInt("123");
# in java, for String to Float, we do:-  float floatStr=Float.parseFloat("234.425");

intToString=str(integerType)            # we convert integer to string type
floatToString=str(floatType)            # we convert flaot to string type
print("\n")
print("We see this ",floatType," change to ",floatToString," with new type: ",type(floatToString))
print("We see this ",integerType," change to ",intToString," with new type: ",type(intToString))

