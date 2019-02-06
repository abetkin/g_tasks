
from pure_utils import pure

class A:

    def __init__(self, **kw):
        self.__dict__.update(**kw)

    @pure
    def f(a, b, c):
        return (a, b, c)


def test_pure():
    kw = {
        'a': 1, 'b': 2, 'c': 3
    }
    obj = A(**kw)
    vals = (1, 2, 3)
    assert A.f(**kw) == vals
    assert A.f(*kw.values()) == vals
    assert obj.f() == vals