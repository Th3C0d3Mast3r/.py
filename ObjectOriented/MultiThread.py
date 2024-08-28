# just as we had multi-threading in java, we even have in python
# thread is like flow of execution. Every thread does its own thing and part
# help to attain concurrency

import threading                                # in-built module of python
import time

print(threading.activeCount())                  # the main thread
print(threading.enumerate())

# NOTES:- These thread do not do anything ACTUALLY PARALLELY. It is virtual
#         The thread runs when the other thread is dormant/not in use

def eatBreakfast():
    time.sleep(9)
    print("BREAKFAST DONE")


def drinkCoffee():
    time.sleep(5)
    print("COFFEE DRANK")

def drinkTea():
    time.sleep(3)
    print("TEA DRANK")

# drinkTea()
# eatBreakfast()
# drinkCoffee()
# so the above was a sequential thing. I had to drink tea, once its sleep elapsed, then breakfast, and then coffee
# thus, only ONE thread was being used for executing the above functions

'''
NOW, FOR MULTI-PROCESSING, WE MAKE THREADS
WE MAKE DIFFERENT THREADS BELOW
'''

t1= threading.Thread(target=eatBreakfast, args=())
t1.start()

t2= threading.Thread(target=drinkCoffee, args=())
t2.start()

t3= threading.Thread(target=drinkTea, args=())
t3.start()

print(threading.active_count())                     # this would give, [ MAIN_THREAD + newThreads ]

# DAEMON THREADS BELOW:-
# they run in background and no wait is needed for that to execute  

def timer():
    print()
    count=0
    while True:
        time.sleep(1)
        count+=1
        print("Logged in for ", count," second[s]")

x=threading.Thread(target=timer, daemon=True)           # N0TE: It is because of daemon, code runs well
x.start()

answer=input("Do You wish to EXIT: ")                   # the moment someone writes anything, the code stops
