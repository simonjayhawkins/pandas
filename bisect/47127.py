# BUG: concat column order behaviors changes after 1.4 #47127

import pandas as pd

print(pd.__version__)

pdf = pd.DataFrame({"A": [0, 2, 4], "B": [1, 3, 5], "C": [6, 7, 8]})
result = pd.concat(
    [pdf, pdf["C"], pdf["A"]], ignore_index=True, join="outer", sort=True
)
print(result)

expected = pd.Index([0, "A", "B", "C"], dtype="object")
pd.testing.assert_index_equal(result.columns, expected)
