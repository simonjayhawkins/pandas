# REGR: ensure DataFrame.select_dtypes() returns a copy #48176

import pandas as pd
from pandas import DataFrame

print(pd.__version__)

# https://github.com/pandas-dev/pandas/issues/48090
# result of this method is not a view on the original dataframe
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df_orig = df.copy()

result = df.select_dtypes(include=["number"])

result.iloc[0, 0] = 0

print(df)

pd.testing.assert_frame_equal(df, df_orig)
