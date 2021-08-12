# BUG: Reindex null timedelta series with pd.Timedelta fails #42921

import pandas as pd

print(pd.__version__)

ts = pd.date_range("2020-01-01", "2020-01-03", freq="1d")
s = pd.Series(pd.Timedelta(None), index=ts)
result = s.reindex(
    pd.date_range("2020-01-01", "2020-01-04", freq="1d"), fill_value=pd.Timedelta(0)
)
print(result)
