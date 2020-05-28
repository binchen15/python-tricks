# chaining of coroutine

# two phases that must be executed in order,
# but that can run concurrently with other operation

import asyncio


async def outer():
    result1 = await phase1()
    result2 = await phase2(result1)
    return (result1, result2)


async def phase1():
    print('in phase1')
    return 'result1'


async def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        return_value = loop.run_until_complete(outer())
        print('return value: {!r}'.format(return_value))
    finally:
        loop.close()
