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
    asyncio.run(main())


'''
Explanation:

    Coroutine (coroutine1 and coroutine2):
        Asynchronous functions defined using async def.
        Simulate asynchronous tasks with await asyncio.sleep().

    Main (main):
        main() function is marked as asynchronous (async def main()).
        It creates two tasks (task1 and task2) using asyncio.create_task().
        asyncio.create_task() schedules the coroutines to run concurrently.

    Awaiting Tasks:
        await task1 suspends main() until coroutine1() completes.
        await task2 suspends main() until coroutine2() completes.
        Both tasks run concurrently due to the event loop managed by asyncio.

    Running the Program:
        The if __name__ == "__main__": block ensures that main() is executed only when the script is run directly.
        asyncio.run(main()) runs the main() coroutine within an event loop.
'''