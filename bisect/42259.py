# BUG: With cache, to_datetime() returns pd.NaT for inputs that produce duplicated values #42259

import pandas as pd

print(pd.__version__)

from pandas import (
    NaT,
    Series,
    Timestamp,
    to_datetime,
)
from pandas._testing import assert_series_equal

input_ser = Series(
    [None] + [NaT] * 50 + ["2012 July 26", Timestamp("2012-07-26")], dtype="object"
)
expected_ser = Series(
    [NaT] * 51 + [Timestamp("2012-07-26"), Timestamp("2012-07-26")],
    dtype="datetime64[ns]",
)
result = to_datetime(input_ser)
print(result)

assert_series_equal(result, expected_ser)
