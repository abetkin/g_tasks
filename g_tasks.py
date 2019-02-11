

import asyncio
import contextvars


class Tasks:
    _tasks = contextvars.ContextVar('tasks', default={})

    def __contains__(self, item):
        return item in self._tasks.get()

    def __getitem__(self, key):
        tasks = self._tasks.get()
        if key in tasks:
            task = tasks[key]
            return task
        loop = asyncio.events.get_event_loop()
        tasks[key] = loop.create_future()
        return tasks[key]


class Context:
    _values = contextvars.ContextVar('values', default={})

    tasks = Tasks()

    def __getattr__(self, item):
        return self._values.get()[item]

    def set_attr(self, key, value):
        values = self._values.get()
        values[key] = value

    def init(self):
        self._values.set({})
        self.tasks._tasks.set({})


g = Context()


class task:

    def __await__(self):
        return self.task

    @property
    def task(self):
        tasks = g.tasks._tasks.get()
        if self.co not in tasks:
            loop = asyncio.events.get_event_loop()
            tasks[self.co] = loop.create_future()
        return tasks[self.co]

    def __init__(self, co):
        self.co = co

    def __call__(self, *args, **kwargs):
        tasks = g.tasks._tasks.get()
        task = asyncio.create_task(self.co())
        if self.co not in tasks:
            tasks[self.co] = task
            return asyncio.shield(task)
        fut = tasks[self.co] #  a future
        task.add_done_callback(lambda r: fut.set_result(r))
        return fut
