# basic file detection-whetehrt the file and folder is there on the System or no
import os

path="F:\\Documents"

if os.path.exists(path):
    print("THE LOCATION AND THE FILE EXISTS")
else:
    print("SUCH FILE AND LOCATION DOESN'T EXIST")

if os.path.isdir(path):
    print("THIS IS A FOLDER")
else:
    print("nothing")