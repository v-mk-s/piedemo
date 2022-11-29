import os
import pickle
from pathlib import Path


def is_int(x):
    try:
        return int(x)
    except:
        return -1


class IntStorage(int):
    pass


class StrStorage(str):
    pass


class FloatStorage(float):
    pass


class FrozenSetStorage(frozenset):
    pass


class DictStorage(dict):
    pass


def make_storage(v):
    return {
        int: IntStorage,
        float: FloatStorage,
        str: StrStorage,
        frozenset: FrozenSetStorage,
        dict: DictStorage,
    }[v.__class__](v)


class Cache(object):
    def __init__(self, path: Path):
        path = Path(path)
        path.mkdir(exist_ok=True)
        stored = set([is_int(p.name[:-4]) for p in path.iterdir() if p.name.endswith('.pkl')])
        if -1 in stored:
            stored.remove(-1)
        self.stored = list(stored)
        self.path = path

    def new_id(self):
        return max(self.stored, default=-1) + 1

    def get(self, data_id):
        data_path = self.path / f"{data_id}.pkl"
        with data_path.open('rb') as f:
            return pickle.load(f)

    def store(self, inputs, outputs):
        data_id = self.new_id()
        data = {
            'inputs': inputs,
            'outputs': outputs
        }
        data_path = self.path / f"{data_id}.pkl"
        with data_path.open('wb') as f:
            pickle.dump(data, f)
        return data_id
