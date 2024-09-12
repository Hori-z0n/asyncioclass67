import time
import asyncio
from asyncio import Queue
from random import randrange

class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

async def checkout_customer(queue: Queue, cashier_number: int):
    total_start_time = time.perf_counter()
    total_customer = 0
    
    while True:
        customer = await queue.get()  # No timeout, block until an item is available
        if customer is None:  # Sentinel value to signal end of processing
            queue.task_done()  # Important to call task_done() for sentinel
            break
        
        customer_start_time = time.perf_counter()
        print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}")
        total_customer += 1
        for product in customer.products:
            print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}'s Product_{product.product_name} in {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
        processing_time = round(time.perf_counter() - customer_start_time, ndigits=2)
        print(f"The Cashier_{cashier_number} finished checkout Customer_{customer.customer_id} in {processing_time} secs")
        
        queue.task_done()

    total_time = round(time.perf_counter() - total_start_time, ndigits=2)
    return cashier_number, total_time, total_customer

def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    # num_products = randrange(0, 5)
    return Customer(customer_id, all_products)

async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while customer_count < customers:
        new_customers = [generate_customer(i) for i in range(customer_count, customer_count+customers)]
        for customer in new_customers:
            print("Waiting to put customer in line....")
            await queue.put(customer)
            print("Customer put in line...")
        customer_count += len(new_customers)
        await asyncio.sleep(0.001)
    
    # Add sentinel values to signal the end of processing
    for _ in range(len(cashiers)):  # One for each cashier
        await queue.put(None)

async def main():
    global cashiers  # Access cashiers from within customer_generation
    customer_queue = Queue(3)
    customer_start_time = time.perf_counter()
    cashiers = [checkout_customer(customer_queue, i) for i in range(5)]
    customer_producer = asyncio.create_task(customer_generation(customer_queue, 10))
    
    # Gather all tasks together
    results = await asyncio.gather(customer_producer, *cashiers)
    
    # Print results
    print(f"The supermarket process finished in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs")
    for cashier in results[1:]:
        print(f"The cashier {cashier[0]} took {cashier[1]} secs and processed {cashier[2]} customers")

if __name__ == "__main__":
    asyncio.run(main())
