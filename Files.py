# This is a file that deals with all the file reading and file writing
# Let's see all about file handling
import shutil                                           # this is the module that we need in the file
try:
    with open('random.txt', 'r') as file:               # Open the file in read mode
        print(file.read())                              # Read and print the file contents

    print(file.closed)                                  # This will print True, as the file is closed after the 'with' block
except Exception as e:
    print("Whoops! The file is not found or there is some typo in the path ", e)

# Now we write into a file
try:
    with open('random.txt', 'w') as file:                # Open the file in write mode (use 'a' for appending)
        file.write("This is the new text that I have added in the file\n")
        file.write("Let's see if something is changing or what!\n")

    # Reading from the file again to see the changes
    with open('random.txt', 'r') as file:
        print(file.read())

except Exception as e:
    print("An error occurred while writing to or reading from the file:", e)


# NOTE:- If you ever WRITE in a file that already has something-it writes after clearing all
# so, in order to UPDATE, the file, you do:-

text="Well, this is the appending in the file"
with open("random.txt", "a") as file:                   # the a is what is APPEND in the file
    file.write(text)


'''COPYING FILES IN PYTHON'''

# we have two or more functions for copying
# copyfile() --> copies the contecnt of the file (the andar ka material of the file)
# copy() --> copyfile() + permission mode + destination can be a directory
# copy2() --> copy() + copies the file's metadata

shutil.copyfile("random.txt", "copy1Random.txt")        # the format is:-  "source", "destination path"
shutil.copy2("random.txt", "copy12Random.txt")

