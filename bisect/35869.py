import numpy as np

import pandas as pd
import pandas.testing as tm

print(pd.__version__)

df = pd.DataFrame(
    {
        "column1": range(6),
        "column2": range(6),
        "group": 3 * ["A", "B"],
        "date": pd.date_range(end="20190101", periods=6),
    }
)
df

res = df.groupby("group").rolling("3d", on="date")["column1"].count()
print(res)

expected = pd.Series(
    np.array([1.0, 2.0, 2.0, 1.0, 2.0, 2.0]),
    pd.MultiIndex.from_arrays(
        [
            ["A"] * 3 + ["B"] * 3,
            pd.DatetimeIndex(
                [
                    "2018-12-27",
                    "2018-12-29",
                    "2018-12-31",
                    "2018-12-28",
                    "2018-12-30",
                    "2019-01-01",
                ],
                dtype="datetime64[ns]",
            ),
        ],
        names=["group", "date"],
    ),
    name="column1",
)

tm.assert_series_equal(res, expected)
