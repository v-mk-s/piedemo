import os
import os
from .base import InputField


class InputChoiceField(InputField):
    def __init__(self,
                 name,
                 choices,
                 enum_type,
                 use_values=False,
                 optional=False):
        super(InputChoiceField, self).__init__(name,
                                               optional=optional)
        self.choices = choices
        self.enum_type = enum_type
        self.use_values = use_values

    def generate(self):
        return {
            "card": "ChoiceCard",
            "data": {
                "name": self.name,
                "optional": self.optional,
                "choices": self.choices,
            }
        }

    def parse(self, data):
        if self.optional and hasattr(data, 'disabled') and data.disabled == 'on':
            return None
        enum_member = getattr(self.enum_type, data)
        if self.use_values:
            return enum_member.value
        return enum_member
