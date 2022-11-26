import io
import base64
from .base import OutputField
import pandas as pd
from typing import Optional


class OutputTableField(OutputField):
    def __init__(self, name):
        super(OutputTableField, self).__init__(name=name)
        self.table: Optional[pd.DataFrame] = None

    def set_output(self, data: pd.DataFrame):
        self.table = data

    def generate(self):
        return {
            "card": "TableCard",
            "data": {
                "name": self.name,
                "headers": self.table.columns.tolist(),
                "rows": [self.table.loc[i].tolist() for i in range(len(self.table))]
            }
        }

    def clear(self):
        self.table = None
