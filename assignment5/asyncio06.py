from random import random
import asyncio

async def task_coro(task, arg): 
    # show what task to do
    print(f"Microwave ({task}): Cooking... {arg}")
    # block for a moment = 1 + random
    await asyncio.sleep(arg)
    # report the value
    print(f'Microwave ({arg}): Finish')
    # return 2 value from function
    return(task, arg)

async def main():
    # Create list of dish
    cook = ['Rice', 'Noodle', 'Curry']
    
    # print(f'Completed task:{done.pop().get_name()}')
    # random value number
    value = random()