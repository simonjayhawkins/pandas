# BUG: DataFrame constructor with copy=False and missing columns creates columns
# that are views of each other #45369

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(index=[1, 2, 3], columns=["a", "b", "c"], copy=False)
df.iloc[0, 0] = 0
print(df)

values = np.full(9, np.nan, dtype=object)
values[0] = 0
values = values.reshape(3, 3)
expected = pd.DataFrame(values, index=[1, 2, 3], columns=["a", "b", "c"])
pd.testing.assert_frame_equal(df, expected)
