import asyncio
from random import random

async def cook(food, t): 
    # show what task to do
    print(f"Microwave ({food}): Cooking {t} seconds...")
    # block for a moment = 1 + random
    await asyncio.sleep(t)
    # report the value
    print(f'Microwave ({food}): Finish')
    # return 2 value from function
    return f'{food} is completed in {t}'

async def main():
    # Create list of dish
    tasks = [asyncio.create_task(cook('Rice', 1 + random())),
             asyncio.create_task(cook('Noodle', 1 + random())),
             asyncio.create_task(cook('Curry', 1 + random()))]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report result
    print(f'Completed task: {len(done)} task.')
    for completed_task in done:
        print(f' - {completed_task.result()}.')
    # print(f'Completed task:{done.pop().get_name()}')
    print(f'Uncompleted task: {len(pending)} tasks.')
    # random value number
    value = random()

if __name__=='__main__':
    asyncio.run(main())