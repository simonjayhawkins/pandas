# BUG: pandas.tseries.offsets.DateOffset behavior changes #45890

import pandas as pd

print(pd.__version__)

s = pd.Series(pd.to_datetime("2022-02-04"))
s = s + pd.DateOffset(1)
print(s)

expected = pd.Series(pd.to_datetime("2022-02-05"))
pd.testing.assert_series_equal(s, expected)
