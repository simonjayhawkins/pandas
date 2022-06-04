# BUG: DatetimeIndex.intersection not working for localized indices #46702

import pandas as pd

print(pd.__version__)

i1 = pd.date_range("2020-03-27", periods=5, freq="D", tz="Europe/Berlin")
i2 = pd.date_range("2020-03-30", periods=5, freq="D", tz="Europe/Berlin")
result = i1.intersection(i2)
print(result)

expected = pd.date_range("2020-03-30", periods=2, freq="D", tz="Europe/Berlin")
pd.testing.assert_index_equal(result, expected)
