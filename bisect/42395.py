# BUG: DataFrame.groupby drops timedelta column in v1.3.0 #42395

import pandas as pd

print(pd.__version__)


df = pd.DataFrame(
    {
        "duration": [pd.Timedelta(i, unit="days") for i in range(1, 6)],
        "value": [1, 0, 1, 2, 1],
    }
)

result = df.groupby("value").sum()
print(result)

expected = pd.DataFrame({"duration": [pd.Timedelta(i, unit="days") for i in [2, 9, 4]]})
expected.index = expected.index.rename("value")

pd.testing.assert_frame_equal(result, expected)
