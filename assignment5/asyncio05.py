from random import random
import asyncio

async def task_coro(arg): 
    # generate a random value between 0 and 1 
    value = random()
    # show what task to do
    print(f"Microwave ({arg}): Cooking... {1+value}")
    # block for a moment = 1 + random
    await asyncio.sleep(1+value)
    # report the value
    print(f'Microwave ({arg}): Finish')
    # return 2 value from function
    return(arg, value+1)

async def main():
    # Create list of dish
    cook = ['Rice', 'Noodle', 'Curry']
    # create many tasks
    tasks = [asyncio.create_task(task_coro(cook[i])) for i in range(0,len(cook))]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report result
    print(f'Completed task: {len(done)} task.')
    # get value from function
    value = done.pop().result()
    # report First task and time result
    print(f'- {value[0]} is completed in {value[1]}')
    # report result
    print(f'Uncompleted task: {len(pending)} tasks.')

asyncio.run(main())