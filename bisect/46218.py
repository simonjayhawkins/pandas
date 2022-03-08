# BUG: pd.cut regression starting in version 1.4.0 when operating on datetime #46218

import pandas as pd

print(pd.__version__)

idx = pd.interval_range(
    pd.Timestamp("2022-02-25"),
    pd.Timestamp("2022-02-27"),
    freq="1D",
)

result = pd.cut(pd.Series([pd.Timestamp("2022-02-26")]), bins=idx).value_counts()
print(result)

dtype = pd.CategoricalDtype(idx, ordered=True)
expected = pd.Series([1, 0], index=idx.astype(dtype))
pd.testing.assert_series_equal(result, expected)
