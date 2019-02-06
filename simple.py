

import asyncio
import typing

from pure_utils import pure

class TaskDef(typing.NamedTuple):
    component: type



import contextvars



class Com:

    _context = contextvars.ContextVar('context')
    #TODO
    _tasks = contextvars.ContextVar('tasks')
    _results = contextvars.ContextVar('results')

    def __init_subclass__(cls, **kwargs):
        cls.task = contextvars.ContextVar('task')
        cls.fut = contextvars.ContextVar('fut')

    @classmethod
    def _launch(cls):
        # TODO check if is launched
        if cls.dep:
            dep_cls = cls.dep.component
            dep_cls._launch()
        t = asyncio.create_task(cls._run())
        cls.task.set(t)

    @classmethod
    async def _run(cls):
        if cls.dep:
            dep_cls = cls.dep.component
            dep_task = dep_cls.task.get()
            dep = await dep_task

            return (await cls.run(dep))

        return (await cls.run())

    @classmethod
    async def run(cls):
        ctx = cls._context.get()
        return ctx[cls]

    @classmethod
    async def eval(cls):
        cls._launch()
        return (await cls._run())


class Date(Com):

    @pure
    async def run():
        await asyncio.sleep(2)
        import datetime
        return datetime.today()

class Name(Com):
    pass

class Greeting(Com):
    dep = TaskDef(Name)

    @pure
    async def run(dep):
        await asyncio.sleep(1)
        return f"Hello, {dep}"


def set_context(dic):
    Com._context.set(dic)


import pytest

@pytest.mark.asyncio
async def test_1():
    set_context({
        Name: "John"
    })
    v = await Greeting.eval()
    print(v)