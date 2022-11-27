import io
import base64
import json
import numpy as np
from .base import OutputField
import pandas as pd
from typing import Optional


class OutputPieGraphField(OutputField):
    def __init__(self, name):
        super(OutputPieGraphField, self).__init__(name=name)
        self.data = None

    def set_output(self, data):
        self.data = data
        assert np.allclose(sum([x['prob'] for x in self.data]), 1)

    def generate(self):
        return {
            "card": "PieGraphCard",
            "data": {
                "name": self.name,
                "distribution": self.data,
            }
        }

    def clear(self):
        self.data = None
