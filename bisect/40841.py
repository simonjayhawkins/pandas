# BUG: AssertionError: <class 'pandas.core.arrays.datetimes.DatetimeArray'> on
# concat #40841

import numpy as np

import pandas as pd
import pandas.testing as tm

print(pd.__version__)

right = pd.DataFrame(
    data={"C": [0.5274]},
    index=pd.DatetimeIndex(
        ["2021-04-08 21:21:14+00:00"],
        dtype="datetime64[ns, UTC]",
        name="Time (UTC)",
        freq=None,
    ),
)

left = pd.DataFrame(
    data={"A": [None], "B": [np.nan]},
    index=pd.Index([None], dtype="object", name="Maybe Time (UTC)"),
)

result = pd.concat([left, right], axis="columns")
print(result)

expected = pd.DataFrame(
    {"A": [None, None], "B": [np.nan, np.nan], "C": [np.nan, 0.5274]},
    index=pd.Index([pd.NaT, pd.Timestamp("2021-04-08 21:21:14+00:00")], dtype="object"),
)

tm.assert_frame_equal(result, expected)
