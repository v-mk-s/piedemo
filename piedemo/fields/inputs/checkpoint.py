import os
from .base import InputField


class InputCheckpointField(InputField):
    def __init__(self, name):
        super(InputCheckpointField, self).__init__(name)

    def generate(self):
        return {
            "card": "TextCard",
            "data": {
                "name": self.name,
            }
        }

    def parse(self, data):
        return str(data)
