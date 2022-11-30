from PIL import Image
import numpy as np


def gen(im: Image.Image):
    squared = Image.fromarray(np.array(im) ** 2)
