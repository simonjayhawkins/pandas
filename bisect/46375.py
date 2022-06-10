# BUG: DataFrameGroupBy.sum() drops column names when applied to an empty dataframe #46375

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(columns=["a", "b", "c"])
result = df.groupby("a", as_index=False).sum()
print(result)

expected = pd.Index(["a", "b", "c"], dtype="object")
pd.testing.assert_index_equal(result.columns, expected)
