import requests
from pprint import pprint as pp
import asyncio ## used for asynchronous work
from aiohttp import ClientSession ## used for asynchronous calls with http

base_url = "http://httpbin.org/"
## Can allows use the base url above to run APIs

async def count():
    for num in [1,2,3,4,5]:
        print(num)
        await asyncio.sleep(1)

async def get_delay(seconds):
    endpoint = f"/delay/{seconds}"
    print(f"Getting with {seconds}s delay ...")

    async with ClientSession() as session:
        async with session.get(base_url+endpoint) as response:
            response = await response.json()
            pp(response)

async def main():
    await asyncio.gather(get_delay(5),count())
## This will run get delay and count at the same time!
asyncio.run(main())

print("All done!")