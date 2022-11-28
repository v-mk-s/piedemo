from .ranged_int import InputRangedIntField


class InputRangedFloatField(InputRangedIntField):
    def __init__(self, name,
                 minValue=0,
                 maxValue=1,
                 stepValue=0.01,
                 formatLabel=''):
        super(InputRangedFloatField, self).__init__(name=name,
                                                    minValue=minValue * int(1 / stepValue),
                                                    maxValue=maxValue * int(1 / stepValue),
                                                    stepValue=1,
                                                    formatLabel=f'/{int(1 / stepValue)}' + formatLabel)
        self.divider = int(1 / stepValue)

    def parse(self, data):
        return super(InputRangedFloatField, self).parse(data) / self.divider
