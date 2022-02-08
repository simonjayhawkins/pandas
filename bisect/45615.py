# BUG: is_bool_dtype 'Series' object has no attribute 'categories' #45615

import pandas as pd

print(pd.__version__)

from pandas import Series
from pandas.core.dtypes.common import is_bool_dtype

s = Series(["foo", "bar", "baz"], dtype="category")
result = is_bool_dtype(s)
print(result)