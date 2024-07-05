import asyncio
from time import sleep, time

async def func_a():
    print("Function A is running")
    await asyncio.sleep(5)
    print("Function A is done")
    return "Function A"

async def func_b():
    print("Function B is running")
    await asyncio.sleep(3)
    print("Function B is done")
    return "Function B"

async def main():
    start = time()
    print("Main function is running")
    results = await asyncio.gather(func_a(), func_b())
    print(f"Main function is done in {time()-start} min")
    print(results)

asyncio.run(main())