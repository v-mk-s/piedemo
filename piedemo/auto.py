import os
import inspect
from PIL import Image
import pandas as pd
import json
import importlib
from .fields.inputs.image import InputImageField
from .fields.inputs.ranged_int import InputRangedIntField
from .fields.inputs.text import InputTextField
from .fields.outputs.base import OutputField
from .fields.outputs.image import OutputImageField
from .fields.grid import VStack
from .fields.outputs.table import OutputTableField
from .fields.outputs.json import OutputJSONField
from typing_extensions import Annotated


def IntRange(minValue,
             maxValue,
             stepValue=1,
             label=""):
    return json.dumps({
        "minValue": minValue,
        "maxValue": maxValue,
        "stepValue": stepValue,
        "formatLabel": label
    })


def input_types2fields(t, **kwargs):
    if isinstance(t, Annotated.__class__):
        kwargs.update(json.loads(t.__metadata__[0]))
        t = t.__args__[0]
    return {
        Image.Image: InputImageField,
        int: InputRangedIntField,
        str: InputTextField
    }[t](**kwargs)


def output_types2fields(t, **kwargs):
    return {
        Image.Image: OutputImageField,
        pd.DataFrame: OutputTableField,
        dict: OutputJSONField,
        list: OutputJSONField,
        int: OutputJSONField,
        float: OutputJSONField,
        type(None): OutputJSONField,
        str: OutputJSONField
    }[t](**kwargs)


def autotyping(dummy_input):
    return {key: type(value) for key, value in dummy_input.items()}


def function2fields(fn):
    input_types = inspect.getfullargspec(fn).annotations
    dummy_input = {k: v() for k, v in input_types.items()}
    dummy_output = fn(**dummy_input)
    output_types = autotyping(dummy_output)

    input_field = VStack([input_types2fields(t, name=k) for k, t in input_types.items()])
    output_field = VStack([output_types2fields(t, name=k) for k, t in output_types.items()])
    return input_field, output_field


def import_function(path):
    module, fn_name = path.split(':')
    module = importlib.import_module(module)
    fn = getattr(module, fn_name)
    return fn, fn_name
