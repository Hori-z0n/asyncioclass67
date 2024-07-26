import time

class Judit:
    pass

class Opponents:
    pass

def Judit_Move():
    print(f"{time.ctime()} - Judit Begin move...")
    time.sleep(0.1)
    print(f"{time.ctime()} -  Judit finish move...")
    return Judit

def Opponents_Move():
    print(f"{time.ctime()} - Opponents Begin move...")
    time.sleep(0.5)
    print(f"{time.ctime()} - Opponents finish move...")
    return Opponents()

def Games(i):
    for move in range(i):
        Judit_Move()
        Opponents_Move()

def Board(i):
    for Competitors in range(i):
        Games(30)
        
if __name__=="__main__":
    start = time.perf_counter()
    Board(1)
    elapsed = time.perf_counter() - start
    print(f"{time.ctime()} - The entrie exhibition takes", elapsed, ".")

