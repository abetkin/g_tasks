
from asyncio import shield
from .pure_utils import pure

class TaskDef:
    pass

class Task:
    pass

'''

Alg:



'''




class Comp:



    @classmethod
    def collect(cls, ns):
        li = []
        for k, v in cls.__dict__.items():
            if isinstance(v, TaskDef):
                li.append(v)
        return li



class Parent:

    @classmethod
    async def from_context(cls, ns):
        task_defs = cls.collect()
        tasks = {
            name: Task(task_def, ns)
            for name, task_def in task_defs.items()
        }
        obj = cls()
        for name, t in tasks:
            v = await shield(t)  # FIXME
            setattr(obj, name, v)
        return obj

    @classmethod
    async def _whole(cls, ctx):
        # obj = Parent()
        obj = await cls.from_context(ctx)
        await obj.run()



class Example:

    @pure
    async def run(self, a, b):
        await new_task


class Datapool:

    token = Token.get_task()

    def get_token(self):
        1

    @pure
    async def task(self):
        await self.get_tasks()


class Image:
    token = Token.task()
    datapool = Datapool.get_task()

