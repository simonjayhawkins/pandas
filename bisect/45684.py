# BUG: Label and integer based indexing return different values for same column #45684

import numpy as np
import pandas as pd

print(pd.__version__)

# create a data frame
# dtypes must be the same for the issue to occur
data = {"x": np.arange(8, dtype=np.int64), "y": np.int64(0)}
df = pd.DataFrame(data)

# These next three lines are necessary to produce the issue.
df = df.copy()
data = df["y"]
df.iat[7, df.columns.get_loc("x")] = 9999

# set the last row of column y to a desired value
df.iat[7, df.columns.get_loc("y")] = 1234

# compare get values for at and iat
atValue = df.at[7, "y"]
iatValue = df.iat[7, df.columns.get_loc("y")]
print(iatValue, atValue, iatValue == atValue)

# inspect data
print("\nThe DataFrame:")
print(df)

print("\nLabel Based:")
print(df["y"])

print("\nInteger Based:")
print(df.iloc[:, df.columns.get_loc("y")])

assert iatValue == atValue
