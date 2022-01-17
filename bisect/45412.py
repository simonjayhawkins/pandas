# BUG: can create IntervalDtype[float32] but not IntervalArray[float32] #45412

import pandas as pd

print(pd.__version__)

try:
    result = pd.core.dtypes.common.pandas_dtype("interval[float32, right]")
    print(result)
except TypeError as e:
    print(e)
else:
    exit(1)
