import os
import numpy as np
from PIL import Image
from .base import InputField


class InputImageField(InputField):
    def __init__(self, name):
        super(InputImageField, self).__init__(name=name)

    def generate(self):
        return {
            "card": "ImageCard",
            "data": {"name": self.name}
        }

    def parse(self, data):
        filestr = data.read()
        npimg = np.fromstring(filestr, np.uint8)
        return Image.fromarray(npimg)
