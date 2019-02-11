
Useless lib

Example

```python
from g_tasks import g, task

@task
async def greet(name):
    return f'Hello, {name}'


async def log():
    return (await greet)


async def main():
    g.init()
    greet('Vitalik')
    print(await log())

```