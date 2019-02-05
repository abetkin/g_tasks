
from pure_utils import pure

from datetime import date

class Mod:

    def run(self):
        return __name__

class Date:

    async def run(self):
        return date.today()


class Message:

    module = Mod.defn()
    date = Date.defn()

    @pure
    def run(self, date, module):
        return f"{module}: {date}"


import pytest

@pytest.mark.asyncio
async def test():
    print(await Message.eval({
        Date: date.today()
    }))