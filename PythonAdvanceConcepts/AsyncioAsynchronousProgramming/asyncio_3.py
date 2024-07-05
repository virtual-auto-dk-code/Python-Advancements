import asyncio


async def my_task(): # an asynchronous coroutine that simulates a task with a 2-second delay
    try:
        await asyncio.sleep(2) # use 12 to raise timeout
        print("Task completed successfully")
        return "Result"
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise
    except Exception as e:
        print(f"Task raised an exception: {e}")


async def main(): # creates a task with asyncio.create_task() and uses asyncio.wait_for() to enforce a timeout of 1 second.
    task = asyncio.create_task(my_task())
    try:
        await asyncio.wait_for(task, timeout=10)  # if timeout 1 then exception
    except asyncio.TimeoutError: # If the task exceeds the timeout, asyncio.TimeoutError is raised and the task is cancelled using task.cancel().
        print("Timeout occurred, cancelling task")
        task.cancel()
        await task


asyncio.run(main())

