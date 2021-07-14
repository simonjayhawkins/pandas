# BUG: isin() with missing values does not work in 1.3.0 with extension dtypes #42405

import pandas as pd

print(pd.__version__)

s = pd.Series([0, None, 2, 3, 4], dtype="Int64")

result = s.isin([1, 2, 3])
print(result)

expected = pd.Series([False, False, True, True, False])

pd.testing.assert_series_equal(result, expected)
