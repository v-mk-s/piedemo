from PIL import Image
import pandas as pd
from piedemo.fields.outputs.image import OutputImageField
from piedemo.webdemo import WebDemo
from piedemo.fields.inputs.image import InputImageField
from piedemo.fields.grid import VStack, HStack


def demo_function(my_input: Image.Image,
                  my_input2: Image.Image):
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


if __name__ == '__main__':
    web = WebDemo("PieDataWebDemo",
                  demo_function=demo_function,
                  inputs=VStack([
                      InputImageField("my_input"),
                      InputImageField("my_input2")
                  ]),
                  outputs=OutputImageField("image"))
    web.run()
