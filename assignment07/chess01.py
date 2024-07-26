
import time 
my_computer_time = 0.1
opponents_compute_time = 0.5
opponents = 1
move_pairs = 30

def game(x):
    # Loops 30 times to simulate both players making a move
    board_start_time = time.perf_counter()
    # print(f"BOARD-{x+1} {i+1} Judit thinking of making a move.")
    # We think for 5 seconds
    for i in range(move_pairs):
        time.sleep(my_computer_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        # The opponents thinks for 5 seconds.
        time.sleep(opponents_compute_time)
        print(f"BOARD-{x+1} {i+1} Opponents made a move.")
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)}")
    return round(time.perf_counter() - board_start_time)
if __name__=="__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    board_time = 0
    for board in range(opponents):
        board_time += game(board)
    # elapsed = time.perf_counter() - start
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")