# BUG: Using .loc with DatetimeIndex drops index name #45818

import pandas as pd

print(pd.__version__)

x = pd.DataFrame(
    {"y": [1, 2, 3]}, index=pd.DatetimeIndex(["2020-01-01", "2020-01-02", "2020-01-03"])
)
x.index.names = ["abc"]

idx = pd.DatetimeIndex(["2020-01-01"])
result = x.loc[idx]
print(result)

# expected = pd.DataFrame({"y": [1]}, index=idx)
# pd.testing.assert_frame_equal(result, expected)
assert result.index.name == "abc"
