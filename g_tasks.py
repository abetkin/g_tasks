

import asyncio
import contextvars


class Tasks:
    _tasks = contextvars.ContextVar('tasks', default={})

    def __contains__(self, item):
        return item in self._tasks.get()

    def __setitem__(self, key, value):
        tasks = self._tasks.get()
        if key not in tasks:
            loop = asyncio.events.get_event_loop()
            tasks[key] = loop.create_future()
        fut = tasks[key]
        fut.set_result(value)

    def __getitem__(self, key):
        tasks = self._tasks.get()
        if key in tasks:
            task = tasks[key]
            return asyncio.shield(task) # ?
        loop = asyncio.events.get_event_loop()
        tasks[key] = loop.create_future()
        print(f'{key}: created')
        return tasks[key]


class Context:
    _values = contextvars.ContextVar('values', default={})

    tasks = Tasks()

    def __getattr__(self, item):
        return self._values.get()[item]

    def set_attr(self, key, value):
        values = self._values.get()
        values[key] = value


g = Context()


class once:

    def __init__(self, co):
        self.co = co

    def __call__(self, *args, **kwargs):
        tasks = g.tasks._tasks.get()
        if self.co in tasks:
            return tasks[self.co]
        task = asyncio.create_task(self.co())
        tasks[self.co] = task
        return asyncio.shield(task)


