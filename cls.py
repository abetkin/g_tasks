
class D:
    def __get__(self, ins, cls):
        return self

    @classmethod
    def __set_name__(*args):
        print('__set_name__', args)


class A():
    @classmethod
    def __init_subclass__(*args):
        print('__init_subclass__', args)



    a = D()


class B(A):

    b = D()


class C(A):

    @classmethod
    def __init_subclass__(*args):
        print('__i.s.__', args)


class E(C):
    pass


with ctx({

})
# await obj.attr