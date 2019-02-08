
import asyncio
import typing

from asyncio_utils import Wait

class TaskDef(typing.NamedTuple):
    component: type


import contextvars

class Component:

    task = contextvars.ContextVar()



    @classmethod
    def defn(cls):
        return TaskDef(cls)

    @classmethod
    def _collect(cls):
        li = []
        for k, v in cls.__dict__.items():
            if isinstance(v, TaskDef):
                li.append(v)
        return li

    @classmethod
    def eval(cls, ns):
        resolve_

    # def


def dispatch(cls, ns):
    deps = cls.get_deps()
    for dep in deps:
        if dep in ns:
            continue
        co = dispatch(dep, ns)
        ns[dep] = asyncio.create_task(co)


class Namespace(dict):
    def resolve(self, *klasses):
        self.resolve_deps(klass)
        klass


    def resolve_deps(self, klass):

    def get_id(self, klass):
        # TODO class may override it's id
        return klass