

import asyncio
import typing

class TaskDef(typing.NamedTuple):
    component: type



import contextvars



class Com:

    task = contextvars.ContextVar('task')

    @classmethod
    def start_task(cls):
        com = cls()
        self.run_com()
        t = asyncio.create_task()
        self.task.set(t)
        if self.dep:
            1

    def _run(self):
        await self.dep.get_task()
        


class Date(Com):
    dep = None

    async def run(self):
        from datetime import date
        return date.today()


class Greet(Com):
    dep = TaskDef(Date)