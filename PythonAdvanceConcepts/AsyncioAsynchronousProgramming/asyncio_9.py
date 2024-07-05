
'''
Error Handling:

    Exceptions raised in coroutines are propagated through await.
    Use try-except blocks within coroutines for error handling.

    Explanation:

    Async Function (main):
        async def main() defines an asynchronous function.
        Inside main, await asyncio.sleep(1) pauses execution for 1 second.
        The raise ValueError('Something went wrong') statement deliberately raises a ValueError exception.
        The except ValueError as e block catches the raised ValueError.

    Error Handling:
        When the ValueError is raised within the try block, control flows to the except block.
        The caught exception (e) is printed using print(f'Error: {e}').

    Running the Program:
        The if __name__ == "__main__": block ensures that asyncio.run(main()) is executed when the script is run directly.
        asyncio.run(main()) runs the main() coroutine within an event loop, handling asyncio tasks and exceptions.

'''

import asyncio

async def main():
    try:
        await asyncio.sleep(1)
        raise ValueError('Something went wrong')
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    asyncio.run(main())
