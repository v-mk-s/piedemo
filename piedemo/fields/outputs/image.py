from .base import OutputField


class OutputImageField(OutputField):
    def __init__(self, name):
        super(OutputImageField, self).__init__(name=name)
