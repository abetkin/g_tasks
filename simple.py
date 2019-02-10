

import asyncio
import contextvars


# future

class Contex:
    tasks = contextvars.ContextVar('tasks', default={})

    def __setitem__(self, key, value):
        tasks = self.tasks.get()
        tasks[key] = value
        # self.tasks.set(tasks)

    def future(self, key):
        1

    def __getitem__(self, key):
        tasks = self.tasks.get()
        return tasks[key]


g = Contex()


from asyncio import events

def _():
    loop = events.get_event_loop()
    loop.create_future()


class once:

    def __init__(self, co):
        self.co = co

    def __call__(self, *args, **kwargs):
        tasks = g.tasks.get()
        if self.co in tasks:
            return tasks[self.co]
        task = asyncio.create_task(self.co())
        tasks[self.co] = task
        return asyncio.shield(task)


