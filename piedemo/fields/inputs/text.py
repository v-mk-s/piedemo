import os
from .base import InputField


class InputTextField(InputField):
    def __init__(self, name):
        super(InputTextField, self).__init__(name)

    def generate(self):
        return {
            "card": "TextCard",
            "data": {
                "name": self.name,
            }
        }

    def parse(self, data):
        return str(data)
