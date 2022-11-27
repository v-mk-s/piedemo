import os
from .base import InputField


class InputRangedIntField(InputField):
    def __init__(self, name,
                minValue=0,
                maxValue=100,
                stepValue=1,
                formatLabel=""):
        super(InputRangedIntField, self).__init__(name)
        self.minValue = minValue
        self.maxValue = maxValue
        self.stepValue = stepValue
        self.formatLabel = formatLabel

    def generate(self):
        return {
            "card": "RangeCard",
            "data": {
                "name": self.name,
                "minValue": self.minValue,
                "maxValue": self.maxValue,
                "step": self.stepValue,
                "formatLabel": self.formatLabel,
                "isRange": False
            }
        }

    def parse(self, data):
        return int(data)
