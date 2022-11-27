import os
import inspect
from PIL import Image
import pandas as pd
import importlib
from .fields.inputs.image import InputImageField
from .fields.outputs.base import OutputField
from .fields.outputs.image import OutputImageField
from .fields.grid import VStack
from .fields.outputs.table import OutputTableField
from .fields.outputs.json import OutputJSONField


input_types2fields = {
    Image.Image: InputImageField
}


output_types2fields = {
    Image.Image: OutputImageField,
    pd.DataFrame: OutputTableField,
    dict: OutputJSONField,
    list: OutputJSONField,
    int: OutputJSONField,
    float: OutputJSONField,
    type(None): OutputJSONField,
}


def autotyping(dummy_input):
    return {key: type(value) for key, value in dummy_input.items()}


def function2fields(fn):
    input_types = inspect.getfullargspec(fn).annotations
    dummy_input = {k: v() for k, v in input_types.items()}
    dummy_output = fn(**dummy_input)
    output_types = autotyping(dummy_output)

    input_field = VStack([input_types2fields[t](name=k) for k, t in input_types.items()])
    output_field = VStack([output_types2fields[t](name=k) for k, t in output_types.items()])
    return input_field, output_field


def import_function(path):
    module, fn_name = path.split(':')
    module = importlib.import_module(module)
    fn = getattr(module, fn_name)
    return fn, fn_name
