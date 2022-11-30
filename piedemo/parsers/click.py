import click
from click import Command
from enum import Enum


def is_click_decorated(fn):
    return isinstance(fn, Command)


def click2types(t):
    if isinstance(t, click.Choice):
        choices = t.choices
        ClickEnum = Enum._create_('ClickEnum', {k: k for k in choices})
        ClickEnum.__piedemo_use_values = True
        return ClickEnum

    return {
        click.INT: int,
        click.FLOAT: float,
        click.STRING: str,
    }[t]


def parse(fn: Command):
    input_types = {p.name: click2types(p.type) for p in fn.params}
    print(fn.callback)
    return input_types, fn.callback
