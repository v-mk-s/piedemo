from PIL import Image
import pandas as pd
from typing_extensions import Annotated
from typing import List, Tuple, Optional
from enum import Enum

from piedemo.fields.outputs.image import OutputImageField
from piedemo.webdemo import WebDemo
from piedemo.fields.inputs.image import InputImageField
from piedemo.fields.grid import VStack, HStack
from piedemo.auto import IntRange


class TestEnum(Enum):
    Enum1 = "Enum1"
    Enum2 = "Enum2"
    Enum3 = "eflk2beqlfnlkwnfqlkfwwq"


def demo_function(my_input: Image.Image,
                  my_input2: Optional[Image.Image]):
    return {
        "image": my_input
    }


def demo_function2(my_input: Image.Image):
    return {
        "table": pd.DataFrame({'a': [1, 2], 'b': [2, 3]})
    }


def demo_function3(my_input: Image.Image):
    return {
        "json1": [1, 2],
        "json2": {'a': 1},
        "json3": {'a': [{'b': 1}]},
        "json4": 1,
    }


def demo_function4(my_input: Optional[Annotated[int, IntRange(0, 100, 4, "sm")]]):
    return {
        "json1": [my_input, 2],
        "json2": {'a': 1},
        "json3": {'a': [{'b': 1}]},
        "json4": my_input ** 2,
    }


def demo_function5(x: Optional[str]):
    return {
        "json": x
    }


def demo_function6(x: Optional[List[int]], y: float):
    return {
        "json": x
    }


def demo_function7(x: Tuple[str, int, str], y: Optional[float]):
    return {
        "json": [list(x), y]
    }


def demo_function8(x: Optional[TestEnum]):
    return {
        "json": str(x)
    }


def demo_function9(x: bool):
    return {
        "json": int(x)
    }


if __name__ == '__main__':
    web = WebDemo("PieDataWebDemo",
                  demo_function=demo_function,
                  inputs=VStack([
                      InputImageField("my_input"),
                      InputImageField("my_input2")
                  ]),
                  outputs=OutputImageField("image"))
    web.run()
