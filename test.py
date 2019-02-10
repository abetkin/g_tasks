
from g_tasks import g, once
from asyncio_utils import Wait

import asyncio

import pytest

@once
async def b():
    await asyncio.sleep(1)
    g.tasks['message'] = 'how are you?'
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
    msg = await g.tasks['message']
    return f"{g.request['params']['greeting']} {msg}"


async def a():
    await asyncio.sleep(1)
    async for _ in Wait(b(), c(), d()):
        pass
    return (await e())



@pytest.mark.asyncio
async def test_1():
    request = {'params': {'greeting': 'Bo!'}}
    g.set_attr('request', request)
    import time
    start = time.time()
    v = await a()
    print(f'time: {time.time() - start}')
    print(v)