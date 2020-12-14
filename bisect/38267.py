import pandas as pd

print(pd.__version__)

s = pd.Series([0, None]).astype("Int64")
result = s.replace(0, pd.NA)
print(result)

expected = pd.Series([None, None]).astype("Int64")

import pandas.testing as tm

tm.assert_series_equal(result, expected)