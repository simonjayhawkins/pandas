# BUG: pandas EWM fails silently if data types are float32 instead of float64 #42452

import numpy as np

import pandas as pd
from pandas import DataFrame
import pandas._testing as tm

print(pd.__version__)

float_dtype = np.float32
df = DataFrame({"A": range(5), "B": range(10, 15)}, dtype=float_dtype)

result = df.rolling(2, axis=1).sum()
print(result)

expected = DataFrame({"A": [np.nan] * 5, "B": range(10, 20, 2)}, dtype=float_dtype)
tm.assert_frame_equal(result, expected, check_dtype=False)
