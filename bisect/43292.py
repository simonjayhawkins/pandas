# BUG: inconsistent result when groupby then sum values that contain inf #43292

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"a": ["hello", "hello", "world", "world"], "b": [np.inf, 10, np.nan, 10]}
)

gb = df.groupby("a")
result = gb.sum()
print(result)

assert result.loc["hello", "b"] == np.inf, result.loc["hello", "b"]
