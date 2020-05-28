# future can be awaited.


import asyncio


def mark_done(future, result):
    future.set_result(result)


async def main(loop):
    future = asyncio.Future()
    loop.call_soon(mark_done, future, 'result')
    result = await future
    print('returned result: {!r}'.format(result))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
