import pandas as pd
import pandas.testing as tm

print(pd.__version__)

s = pd.Series([1, 2, 3])
original = s.copy()
s1 = s.iloc[1:]
s1 -= 4
print(s)
tm.assert_series_equal(s, original)
