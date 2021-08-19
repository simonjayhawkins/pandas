# BUG: Change of behavior in casting of datetime-like types in MultiIndex #43091

import datetime

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "date": [
            datetime.date(2021, 8, 1),
            datetime.date(2021, 8, 2),
            datetime.date(2021, 8, 3),
        ],
        "ticker": ["aapl", "goog", "yhoo"],
        "value": [5.63269, 4.45609, 2.74843],
    }
)
df.set_index(["date", "ticker"], inplace=True)

result = df.index.get_level_values(0)
print(result)

expected = pd.DatetimeIndex(
    ["2021-08-01", "2021-08-02", "2021-08-03"],
    dtype="datetime64[ns]",
    name="date",
    freq=None,
)

pd._testing.assert_index_equal(result, expected)
