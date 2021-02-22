# BUG: unary operators on IntegerArray return shared mask creating inconsistencies when assigning null and non-null values #39943

import pandas as pd
import pandas.testing as tm

print(pd.__version__)

s = pd.Series([1, 2, 3], dtype="Int64")
s2 = -s
expected = s2.copy()
s[0] = None
print(s2)
tm.assert_series_equal(s2, expected)
