# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
import multiprocessing
import os
from time import sleep, ctime, time

def cooking(index):
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index} : Begin cooking..PID{os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen-{index} : Cooking done in {duration:0.2f} seconds')

def kitchen(index):
     cooking(index)

if __name__ == "__main__":
    # Begin of main thread
    print(f'{ctime()} Main   :start Cooking...PID{os.getpid()}')
    start_time = time()
    kitchens = list()

    # Multi kitchens with each chef
    for index in range(200):
        p = multiprocessing.Process(target=kitchen, args={index, })
        kitchens.append(p)
        # starting process
        p.start()
    for index, p in enumerate(kitchens):
        # wait until processes are finished
        p.join

    duration = time() - start_time
    print(f"{ctime()} Main : Finished Cooking duration in {duration:0.2f} seconds")
