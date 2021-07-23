# BUG: SeriesGroupBy.value_counts() throws IndexError if there is only one group #42618

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([[0, 1]], columns=("a", "b"))
grp = df.groupby("a")["b"]
result = grp.value_counts()
print(result)

expected = pd.Series(
    [1], index=pd.MultiIndex.from_tuples([(0, 1)], names=["a", "b"]), name="b"
)
pd.testing.assert_series_equal(result, expected)
