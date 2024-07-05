import asyncio

'''
Coroutines:

    Asynchronous functions
    defined in Python using async def.
    They can pause their execution using await, allowing other tasks to run in the meantime.
'''

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('In my Asynchronous World')

asyncio.run(main())







#
