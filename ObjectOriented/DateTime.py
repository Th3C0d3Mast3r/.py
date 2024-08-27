# this is a file that deals with some in-built time and date functions
# we will be using in-built date-time functions of python, just as we had in Java as well

import time                                             # this is an in-built module
print(time.ctime(0))                                    # this tells us the epoch of the system(the t=0 for computer)
#                                                         the above may vary from computer-to-computer

print(time.time())                                      # the seconds past epoch time(not worth or usable for you)

# for current time, we do:-
print(time.ctime(time.time()))                          # METHOD-1
times=time.localtime()                                  # this is an object having diff sub-things of this
# print(times)                                            to see the struct of time object
localtime=time.strftime("%B %d, %Y | %H:%M:%S", times)
print(localtime)

timeTuple=(2020, 4, 20, 4, 20, 45, 3, 2, 0)             # format => year, month, date, hour, min, sec, dayNo
timeString=time.asctime(timeTuple)

print(timeString)

# well, this is something wide and has lots of things. Thus, refer to documentation and external references

'''
some official Python Documentations for the same:-
- https://docs.python.org/3/library/time.html
- https://docs.python.org/3/library/datetime.html
'''