# this is something we had not done in Java
# hopefully this is something new and we get to learn more things

# these two are the required Modules for running multi-processing
import multiprocessing 
from multiprocessing import Process,  cpu_count
import time

def counter(num):
    count=0
    while count<num:
        count+= 1
    
# when we ran just a process a to reach to 1000, it took 0.3085832 seconds to run
# now, when we use two processes, we observe:-
def main():

    print("TOTAL CPU COUNTS POSSIBLE:- ", cpu_count())

    a=Process(target=counter, args=(2000,))
    # b=Process(target=counter, args=(500,))
    # c=Process(target=counter, args=(500,))
    # d=Process(target=counter, args=(500,))

    a.start()
    # b.start()
    # c.start()
    # d.start()

    a.join()
    # b.join()
    # c.join()
    # d.join()

    print("FINISHED IN: ", time.perf_counter(), " seconds")

if __name__== '__main__':
    main()


