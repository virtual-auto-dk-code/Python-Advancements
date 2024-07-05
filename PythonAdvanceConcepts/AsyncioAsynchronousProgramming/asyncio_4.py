import asyncio

async def io_task(num): # an asynchronous coroutine that prints and waits for 1 second, simulating an IO-bound task.
    print(f"Starting IO task {num}")
    await asyncio.sleep(1)
    print(f"Finished IO task {num}")

async def main(): # creates a list of tasks (io_task(1), io_task(2), io_task(3)) and waits for all tasks to complete concurrently with asyncio.gather().
    tasks = [io_task(i) for i in range(1, 4)]
    await asyncio.gather(*tasks)

asyncio.run(main())
