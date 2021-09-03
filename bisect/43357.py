# BUG: #43357

import pandas as pd

print(pd.__version__)


def func(a, b, c=2):
    return a, b, c


s = pd.Series([1, 2, 3, 4])

result = s.aggregate(func, 0, 99, c=101)
print(result)
