# QUICK TIP BEFORE YOU START-
# if you are using VSCode, then, run codes hence this on Terminal (ctrl+`) 
# write this command:-  python <fileName>.py

# this is the file that teaches how to take user input in Python
'''
In Java, for taking the user input, these are the basic steps:- 

import java.util.*;
class UserInput
{
    Scanner obj=new Scanner(System.in);
    public static void main(String args[])
    {
        System.out.println("Enter Text below:- ");
        String randomText=obj.nextLine();
    }
}
'''
# this is how this is done in python:-
randomText=input("Enter a Random Text: ")
print("You Entered the Random Text:- "+randomText)

# the down side of inputs in Python is that, it takes input in String format only
# so an Explicit Type Conversion is needed for this to happen

age=int(input("Enter Your Age: "))
print("So You are ",age," Years Old")

# the same would even go for float datatype