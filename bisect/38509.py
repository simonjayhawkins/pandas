import pandas as pd
import pandas.testing as tm

print(pd.__version__)

tdi = pd.timedelta_range("1 Day", periods=3)
ser = pd.Series(tdi)
result = ser.astype("string")
print(result)

expected = pd.Series(["1 days", "2 days", "3 days"], dtype="string")

tm.assert_series_equal(result, expected)
