from random import random
import asyncio

async def task_coro(arg): 
    # random value number
    value = random()
    print(f"Microwave ({arg}): Cooking... {1+value}")
    await asyncio.sleep(1+value)
    print(f'Microwave ({arg}): Finish')
    # return value from function
    return(arg, value+1)

async def main():
    # Create list of dish
    cook = ['Rice', 'Noodle', 'Curry']
    tasks = [asyncio.create_task(task_coro(cook[i])) for i in range(0,3)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f'Completed task: {len(done)} task.')
    # print(f'Completed task:{done.pop().get_name()}')
    value = done.pop().result()
    print(f'- {value[0]} is completed in {value[1]}')
    print(f'Uncompleted task: {len(pending)} tasks.')

asyncio.run(main())