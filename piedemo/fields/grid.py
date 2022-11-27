import os
from .base import Field


class VStack(Field):
    def __init__(self, fields):
        super(VStack, self).__init__(None)
        self.fields = fields

    def generate(self):
        return [[{"content": f.generate(), "xs": ""}] for f in self.fields]

    def children(self):
        return sum([f.children() for f in self.fields], [])

    def clear(self):
        for f in self.fields:
            f.clear()

    def __repr__(self):
        return "VStack([%s])" % ',\n'.join([repr(f) for f in self.fields])


class HStack(Field):
    def __init__(self, fields):
        super(HStack, self).__init__(None)
        self.fields = fields

    def generate(self):
        return [[{"content": f.generate(), "xs": ""} for f in self.fields]]

    def children(self):
        return sum([f.children() for f in self.fields], [])

    def clear(self):
        for f in self.fields:
            f.clear()

    def __repr__(self):
        return "HStack([%s])" % ',\n'.join([repr(f) for f in self.fields])
