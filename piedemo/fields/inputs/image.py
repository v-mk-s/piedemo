import os
import numpy as np
from PIL import Image
import cv2
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
        return Image.open(data)
