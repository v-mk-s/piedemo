import os
from .base import InputField


class InputTextField(InputField):
    def __init__(self, name,
                 optional=False):
        super(InputTextField, self).__init__(name,
                                             optional=optional)

    def generate(self):
        return {
            "card": "TextCard",
            "data": {
                "name": self.name,
                "optional": self.optional
            }
        }

    def parse(self, data):
        if self.optional and hasattr(data, 'disabled') and data.disabled == 'on':
            return None

        return str(data)
