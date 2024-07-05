'''
Concurrency with await:

    Use await to pause execution until a coroutine completes.
    Allows non-blocking I/O operations to run concurrently without threads.
'''

import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    data = await fetch_data(url)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
'''
Explanation:

    Async Function (fetch_data):
       async with aiohttp.ClientSession() as session: creates an asynchronous HTTP session using aiohttp.
        async with session.get(url) as response: sends an asynchronous GET request to the specified URL and asynchronously waits for the response.
        await response.text() reads the response body as text asynchronously and returns it.

    Main Function (main):
        async def main() is another asynchronous function that serves as the entry point.
        It defines a URL (url) from which data will be fetched asynchronously using fetch_data.
        data = await fetch_data(url) asynchronously calls fetch_data to fetch data from the URL and waits for it to complete.
        print(data) prints the fetched data to the console.

    Running the Program:
        The if __name__ == "__main__": block ensures that asyncio.run(main()) is executed when the script is run directly.
        asyncio.run(main()) runs the main() coroutine in the asyncio event loop, managing the asynchronous execution of tasks.
'''