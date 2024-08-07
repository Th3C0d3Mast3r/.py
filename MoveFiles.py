import os

source="test.txt"
destination="F:\\Documents"

try:
    if os.path.exists(destination):
        print("SOME FILE ALREADY EXISTS")
    else:
        print("NO FILE FOUND. GOOD TO GO")
        os.replace(source, destination)
        print("MOVED SUCCESSFULY")
except Exception as e:
    print("Error Occured-", e)  

# to delete a file, this is the code:-  try: os.remove(filepath)
# well, there are actually 3 such functions for file deleting:-
# 1) os.remove()        2) os.rmdir()       3) shutil.remtree()
# delete a file     delete empty directory  delete directory + files within