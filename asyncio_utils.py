import asyncio

class Wait:
    '''
    Async iterator, constructed from a list of awaitables.
    Returns results or exceptions as soon as they are ready.
    '''

    def __init__(self, *awaitables):
        loop = asyncio.events.get_event_loop()
        self.results = [
            loop.create_future()
            for _ in awaitables
        ]

        def on_done(f, results=self.results[:]):
            results.pop().set_result(f)

        for task in awaitables:
            task.add_done_callback(on_done)

    def __aiter__(self):
        return self

    async def __anext__(self):
        while self.results:
            fut = self.results.pop()
            fut = await fut
            if fut.cancelled():
                return asyncio.CancelledError()
            return fut.exception() or fut.result()
        raise StopAsyncIteration