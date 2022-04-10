# BUG: loc with MultiIndex as index is returning incorrect Index #46704

import pandas as pd

print(pd.__version__)

s = pd.DataFrame({"a": [1, 1, 2], "b": [1, 2, 3], "c": ["a", "b", "c"]}).set_index(
    ["a", "b"]
)["c"]

result = s.loc[(1, slice(None))]
print(result)

expected = s.iloc[:2]
pd.testing.assert_series_equal(result, expected)
