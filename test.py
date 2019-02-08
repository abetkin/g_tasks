
from simple import g
from asyncio_utils import Wait

import asyncio

import pytest

@once
async def b():
    await asyncio.sleep(1)
    return 1

@once
async def c():
    await asyncio.sleep(1)
    return 1

@once
async def d():
    await asyncio.sleep(1)
    return 1

@once
async def e():
    await asyncio.sleep(1)
    r =  (g >> Request)
    return r['params']


async def a():
    await asyncio.sleep(1)
    async for _ in Wait(
            g >> b,
            g >>c,
            g >> d):
        pass
    return (await g >> e)


from util import Request

@pytest.mark.asyncio
async def test_1():
    # TODO once decorator
    g[Request] = {'params': {'hey': '!'}}
    import time
    start = time.time()
    v = await a()
    print(f'time: {time.time() - start}')
    print(v)