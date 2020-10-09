import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"col": range(10)}, index=pd.date_range("2012-01-01", periods=10, freq="20min")
)

res = df.resample("H").apply(lambda group: len(group["col"].unique()))
print(res)

index = pd.DatetimeIndex(
    [
        "2012-01-01 00:00:00",
        "2012-01-01 01:00:00",
        "2012-01-01 02:00:00",
        "2012-01-01 03:00:00",
    ],
    dtype="datetime64[ns]",
    freq="H",
)

expected = pd.Series([3, 3, 3, 1], index=index)

import pandas.testing as tm

tm.assert_series_equal(res, expected)

res2 = df.resample("H").apply(lambda group: len(group.col.unique()))
print(res2)

tm.assert_series_equal(res2, expected)
