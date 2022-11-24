import os


class Field(object):
    def __init__(self, name):
        self.name = name

    def generate(self):
        raise NotImplementedError()

    def children(self):
        return [self]

    def clear(self):
        pass
