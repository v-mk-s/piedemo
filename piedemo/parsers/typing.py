import inspect


def parse(fn):
    input_types = inspect.getfullargspec(fn).annotations
    return input_types, fn
