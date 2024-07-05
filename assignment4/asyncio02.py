# example of starting many tasks and getting access to all tasks
import asyncio
async def task_coroutine(value):
    print(f'task {value} is running')
    await asyncio.sleep(1)

async def main():
    print('main coroutine started')

    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    await asyncio.sleep(0.1)
    tasks = asyncio.all_tasks()

    for task in tasks:
        print(f'>{task.get_name()}, {task.get_coro}')

    for task in started_tasks:
        await task

asyncio.run(main())