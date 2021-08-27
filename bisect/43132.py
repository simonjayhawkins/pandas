# BUG: timeseries.groupby(...).transform('mean') wrong when aggregating over pd.NaT #43132

import pandas as pd

print(pd.__version__)

s = pd.Series(["1 day", "3 days", pd.NaT], dtype="timedelta64[ns]")
grp = s.groupby([1, 1, 1])
try:
    result = grp.transform("mean")
    print(result)
    assert False
except pd.core.base.DataError as e:
    print(e)
