import os
from ..base import Field


class InputField(Field):
    def __init__(self, name):
        super(InputField, self).__init__(name=name)
