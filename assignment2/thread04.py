import os
from time import time, ctime, sleep
import threading

def cube(n):
    print("Cube: {}".format(n*n*n))

def square(n):
    print("Square: {}".format(n*n))

if __name__=="__main__":
    t1 = threading.Thread(target=square, args=(10, ))

    t2 = threading.Thread(target=cube, args=(10, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")