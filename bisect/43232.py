# BUG: reorder_categories with inplace=True is not changing the dtype.categories #43232

import pandas as pd

print(pd.__version__)

sr = pd.Series(["a", "b", "c"], dtype="category")

sr.cat.reorder_categories(["c", "b", "a"], inplace=True)
print(sr)

result = sr.dtype.categories
expected = pd.Index(["c", "b", "a"], dtype="object")
pd.testing.assert_index_equal(result, expected)
