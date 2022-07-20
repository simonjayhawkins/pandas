# BUG: Inconsistency in DataFrame.where between inplace and not inplace with na like value
# for StringArray #46512

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"A": ["1", "", "3"]}, dtype="string")
df.where(df != "", np.nan, inplace=True)
print(df)
arr = df["A"]._values
print(arr)
assert arr[1] is np.nan, type(arr[1])
