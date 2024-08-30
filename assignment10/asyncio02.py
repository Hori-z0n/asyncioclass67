# example of using an asyncio queue without blocking
from random import random
import asyncio
import time
# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    start_time = time.perf_counter()
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    end_time = time.perf_counter()
    print(f"{time.ctime()} Producer {value+1} Time taken: {end_time-start_time} seconds")
    print('Producer: Done')
 
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    start_time = time.perf_counter()
    # consume work
    sleep_time = 0.5
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(sleep_time)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')    
    end_time = time.perf_counter()
    print(f"{time.ctime()} consumer all use Time taken: {end_time-start_time} seconds")
    # all done
    print('Consumer: Done')
 
# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    start_time = time.perf_counter()
    await asyncio.gather(producer(queue), consumer(queue))
    end_time = time.perf_counter()
    print(f"{time.ctime()} Time taken: {end_time-start_time} seconds")

    
# start the asyncio program
asyncio.run(main())