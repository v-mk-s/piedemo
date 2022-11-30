from piedemo.parsers.func_scope import func2locals
from examples.no_return_webapp import f


print(func2locals(f)(**{'a': 1, 'c': 12}))
