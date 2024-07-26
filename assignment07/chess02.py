import asyncio
import time

my_computer_time = 0.1
opponents_compute_time = 0.5
opponents = 24
move_pairs = 30

# Again notice that I declare the main() function as a async function
async def main(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        # Don't use time.sleep in a async function. I'm using it because in reality you aren't thiking about 
        # move on 24 board at the same time, and so I need to block the event loop.
        time.sleep(my_computer_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        await asyncio.sleep(opponents_compute_time)
        # Here our opponent is making their turn and now we can move onto the next board.
        print(f"BOARD-{x+1} {i+1} Opponents made a move.")
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)}")
    return round(time.perf_counter() - board_start_time)

async def async_io():
    # Again same structure as in async-io.py
    start_time = time.perf_counter()
    board_time = 0
    task = []
    for i in range(opponents):
        task += [main(i)]
    await asyncio.gather(*task)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} secs.")

    # This is how I make task but I not use it now
    # tasks = [asyncio.create_task(main(board)) for board in range(opponents)]
    # done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # print(f"Board exhibition finished in {board_time} secs.")
    # print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

if __name__=='__main__':
    start_time = time.perf_counter()
    asyncio.run(async_io())

    
