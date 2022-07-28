# BUG: Update Values from MultiIndex Dataframe after using loc is not applied correctly #47867

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame()
df["idx1"] = [0, 1, 2, 3, 4]
df["idx2"] = [0, 1, 2, 3, 4]
df["abool"] = True
df["a"] = np.arange(5, dtype="int64")
df["b"] = np.arange(5, dtype="float64")
df["c"] = np.arange(5, dtype="int64")
df = df.set_index(["idx1", "idx2"])

idx = [(1, 1), (3, 3)]
df.loc[idx, "c"] = 0
df.loc[idx, "c"]

df.loc[idx, ["a", "b"]]  # This line is the problem

df.loc[idx, "c"] = 15
result = df.loc[idx, "c"]
print(result)
# idx1  idx2
# 1     1       15
# 3     3       15
# Name: c, dtype: int64

# incorrect result to find fix
expected = pd.Series(
    [0, 0], index=pd.MultiIndex.from_tuples(idx, names=["idx1", "idx2"]), name="c"
)

pd.testing.assert_series_equal(result, expected)
