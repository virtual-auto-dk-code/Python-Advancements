import asyncio
import aiohttp


async def fetch_url(session, url):  # an asynchronous coroutine using aiohttp to fetch the content of a URL.
    async with session.get(url) as response:
        return await response.text()


async def main():  # creates a list of URLs and uses aiohttp.ClientSession() to manage HTTP connections.
    urls_ls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_url(session, url)) for url in
                 urls_ls]  # creates tasks for each URL using asyncio.create_task()
        results = await asyncio.gather(*tasks)  # gathers results with asyncio.gather().
        for result in results:
            print(result)


asyncio.run(main())  # runs the main() coroutine within an asyncio event loop.