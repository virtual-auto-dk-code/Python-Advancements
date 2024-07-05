import asyncio


async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(2)  # Simulating some asynchronous task
    print("Coroutine 1 finished")


async def coroutine2():
    print("Coroutine 2 started")
    await asyncio.sleep(1)  # Simulating another asynchronous task
    print("Coroutine 2 finished")


async def main():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())

    # Await both tasks concurrently
    await task1
    await task2


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


'''
Explanation:

    Coroutine Definitions (coroutine1 and coroutine2):
        These are asynchronous functions defined using async def.
        They simulate asynchronous tasks with await asyncio.sleep().

    Main Function (main):
        main() function is marked as asynchronous (async def main()).
        It creates two tasks (task1 and task2) using asyncio.create_task().
        asyncio.create_task() schedules the coroutines to run concurrently.

    Event Loop:
        loop = asyncio.get_event_loop() retrieves the event loop.
        loop.run_until_complete(main()) runs the main() coroutine until it completes.
        This blocks the program until all tasks (task1 and task2) have finished execution.

    Run Program:
        The if __name__ == "__main__": block ensures that main() is executed only when the script is run directly.
        The event loop (loop) manages the execution of asynchronous tasks (coroutine1() and coroutine2()).
'''