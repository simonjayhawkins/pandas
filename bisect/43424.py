# BUG: Series.fillna raising with float32 dtype when using value arg #43424

import pandas as pd

print(pd.__version__)

ser = pd.Series([1.0, 2.0], dtype="float32")
val = {1: 1.01}
result = ser.fillna(val)
print(result)

pd.testing.assert_series_equal(result, ser)
