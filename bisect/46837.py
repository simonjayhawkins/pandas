# BUG: Setting multiple values via .loc produces NaNs with MultiIndex #46837

import pandas as pd

print(pd.__version__)

i = pd.MultiIndex.from_product([(0, 1), (2, 3)])
s = pd.Series([True] * 4, index=i)

expected = s.copy()

s.loc[0, :] = s.loc[0, :]
print(s)

pd.testing.assert_series_equal(s, expected)
