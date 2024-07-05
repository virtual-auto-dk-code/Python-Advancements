import asyncio


async def producer(queue, num): # produces items (item-0 to item-4) into a queue every second.
    for i in range(num):
        await asyncio.sleep(1)
        item = f"item-{i}"
        await queue.put(item)
        print(f"Produced {item}")


async def consumer(queue): # consumes items from the queue, processing each item every 2 seconds.
    while True:
        item = await queue.get()
        await asyncio.sleep(2)
        print(f"Consumed {item}")
        queue.task_done()


async def main(): # creates tasks for both producer() and consumer() and uses asyncio.Queue() to manage the communication between them.
    queue = asyncio.Queue()

    # an asynchronous coroutine that
    producer_task = asyncio.create_task(producer(queue, 5)) # produces items (item-0 to item-4) into a queue every second.
    consumer_task = asyncio.create_task(consumer(queue)) # consumes items from the queue, processing each item every 2 seconds.

    await asyncio.gather(producer_task)
    await queue.join() # an asynchronous method that blocks the coroutine until all items that have been put() into the queue have been get() and processed.
    consumer_task.cancel()


asyncio.run(main())

