import datetime

import pandas as pd
import pandas.testing as tm

print(pd.__version__)


df = pd.DataFrame(
    {
        "A": ["X", "Y"],
        "B": [
            datetime.datetime(2005, 1, 1, 10, 30, 23, 540000),
            datetime.datetime(3005, 1, 1, 10, 30, 23, 540000),
        ],
    }
)
print(df)

print(df.dtypes)

result = df.groupby("A").B.max()
print(result)

expected = pd.Series(
    [
        pd.Timestamp("2005-01-01 10:30:23.540000"),
        datetime.datetime(3005, 1, 1, 10, 30, 23, 540000),
    ],
    index=pd.Index(["X", "Y"], dtype="object", name="A"),
    name="B",
)

tm.assert_series_equal(result, expected)
