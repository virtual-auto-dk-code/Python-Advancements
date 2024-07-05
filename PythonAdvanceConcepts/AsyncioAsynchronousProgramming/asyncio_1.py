import asyncio


# an asynchronous coroutine that simulates a delay with asyncio.sleep() and prints a greeting.
async def say_hi(delay, name):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")


'''
Coroutines: In Python, a coroutine is a function defined with async def.
It allows to use await within the function body to pause its execution until some condition is met (typically until an I/O operation completes).
'''
async def main():
    # Schedule coroutines to run concurrently
    task_1 = asyncio.create_task(say_hi(2, "I"))  # creates tasks for say_hello() with different delays.
    task_2 = asyncio.create_task(say_hi(1, "Me"))

    # Wait for all tasks to complete
    await asyncio.gather(task_1, task_2)  # waits for all tasks to complete concurrently.


asyncio.run(main())  # runs the main() coroutine within an asyncio event loop.
