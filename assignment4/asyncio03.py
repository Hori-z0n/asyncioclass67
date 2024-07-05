# example of gather for many coroutines in a list
import asyncio
async def task_coro(value):
    print(f't>ask {value} executing')
    await asyncio.sleep(1)

async def main():
    print('main starting')

    coros = [task_coro(i) for i in range(10)]

    await asyncio.gather(*coros)
    
    print('main done')

asyncio.run(main())