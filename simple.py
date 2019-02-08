

import asyncio
import contextvars

class Contex:
    tasks = contextvars.ContextVar('tasks', default={})

    def __rshift__(self, coro):
        tasks = self.tasks.get()
        if coro in tasks:
            return tasks[coro]
        task = asyncio.create_task(coro())
        tasks[coro] = task
        return asyncio.shield(task)

    def __setitem__(self, key, value):
        tasks = self.tasks.get()
        tasks[key] = value
        self.tasks.set(tasks)

g = Contex()



import pytest

@pytest.mark.asyncio
async def test_1():
    set_context({
        Name: "John"
    })
    v = await Greeting.eval()
    print(v)