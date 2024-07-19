import time
import asyncio
class Coffee:
    pass

class Egg:
    pass

class Bacon:
    pass

class Toast:
    pass

class Juice:
    pass

def PourCoffee():
    print(f"{time.ctime()} - Begin pour coffee...")
    time.sleep(2)
    print(f"{time.ctime()} - finish pour coffee...")
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} - Begin apply butter...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} - Finish apply butter...")

async def FryEggs(eggs):
    print(f"{time.ctime()} - Begin fry eggs...")
    print(f"{time.ctime()} - heat pan to fry eggs...")
    await asyncio.sleep(1)
    for egg in range(eggs):
        print(f"{time.ctime()} - Frying", egg+1, "eggs")
        await asyncio.sleep(1)
    print(f"{time.ctime()} - Finish fry eggs...")
    print(f"{time.ctime()} - >>>>>>>> Fry eggs are ready...")
    return Egg()

async def FryBeacon():
    print(f"{time.ctime()} - Begin fry bacon...")
    await asyncio.sleep(2)
    print(f"{time.ctime()} - Finish fry bacon...")
    print(f"{time.ctime()} - >>>>>>>> Fry eggs are ready...")
    return Bacon()

async def ToastBread(slices):
    for slice in range (slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        await asyncio.sleep(1)
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        await ApplyButter()
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
    print(f"{time.ctime()} - >>>>>>> Toast are ready\n")
    return Toast()

def PourJuice():
    print(f"{time.ctime()} - Begin pour juice...")
    time.sleep(1)
    print(f"{time.ctime()} - Finish pour juice...")
    return Juice()

async def main():
    PourCoffee()
    print(f"{time.ctime()} - >>>>>>>> Coffee is ready\n")
    tasks = [
             asyncio.create_task(FryEggs(2)),
             asyncio.create_task(FryBeacon()),
             asyncio.create_task(ToastBread(2))
             ]
    done, pending = await asyncio.wait(tasks)
    print(f"\n{time.ctime()} - >>>>>>>> Nealy to finished\n")
    PourJuice()

if __name__=="__main__":
    start_cooking = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} - Breakfast cooked in", elapsed, "seconds.")