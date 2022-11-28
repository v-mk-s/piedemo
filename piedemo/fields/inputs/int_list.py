import os
import os
from .base import InputField


class InputIntListField(InputField):
    def __init__(self, name):
        super(InputIntListField, self).__init__(name)

    def generate(self):
        return {
            "card": "TagsCard",
            "data": {
                "name": self.name,
                "isIntOnly": True,
            }
        }

    def parse(self, data):
        return list(map(int, data.split(', ')))
