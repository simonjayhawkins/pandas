# BUG: Inconsistent assignment of NAT values to datetime columns in MultiIndex #43351

import numpy as np

import pandas as pd

print(pd.__version__)

midx = pd.MultiIndex(
    [
        ["a", "b", "c"],
        ["house", "store", "forest"],
        ["clouds", "clear", "storm"],
        ["fire", "smoke", "clear"],
        [
            np.datetime64("2001-01-01", "ns"),
            np.datetime64("2002-01-01", "ns"),
            np.datetime64("2003-01-01", "ns"),
        ],
        [1.0, np.nan, 2],
    ],
    [
        [0, 0, 0, 0, 1, 1, 2],
        [1, 1, 1, 1, 0, 0, 2],
        [0, 0, 2, 2, 2, 0, 1],
        [0, 0, 0, 1, 2, 0, 1],
        [1, 0, 1, 2, 0, 0, 1],
        [1, 0, 1, 2, 0, 0, 1],
    ],
)
midx.names = ["alpha", "location", "weather", "sign", "timestamp", "float"]
pdf = pd.DataFrame(
    {"a": [1], "b": [2], "c": [3], "d": [2], "e": [0], "f": [2], "g": [10]}
)
pdf.columns = midx
pdf["new_col"] = [11]

result = pdf["new_col"]
print(result)

expected = pd.Series([11], dtype=np.int64, name="new_col")
pd.testing.assert_series_equal(result, expected)
