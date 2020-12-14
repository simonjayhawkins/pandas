import sys

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    [[1, 2], [3, 4], [5, 6]], index=pd.date_range("2020-01-30", "2020-02-01")
)

result = df.resample("1M").apply(lambda df: df.mean().mean())
print(result)

expected = pd.Series(
    [2.5, 5.5],
    index=pd.DatetimeIndex(
        ["2020-01-31", "2020-02-29"], dtype="datetime64[ns]", freq="M"
    ),
)

import pandas.testing as tm

try:
    tm.assert_series_equal(result, expected)
except:
    pass
else:
    sys.exit(1)
