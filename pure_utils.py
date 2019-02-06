

import inspect

class pure:

    def __init__(self, f):
        self.f = f

    def __get__(self, ins, cls):
        if not ins:
            return self.f
        sig = inspect.signature(self.f)
        param_names = list(sig.parameters)
        params = [
            getattr(ins, k) for k in param_names
        ]
        return lambda: self.f(*params)
