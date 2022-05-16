# BUG: dataframe with datetimeindex as index, when indexing columns interprets some strings as datetimes #47006

import pandas as pd

print(pd.__version__)

index = pd.DatetimeIndex(
    [pd.to_datetime("2035-01-01 01:00:00"), pd.to_datetime("2036-01-01 00:00:00")]
)
df = pd.DataFrame(index=index)

try:
    df.loc[:, "110735"] = 0
except KeyError as e:
    print(e)
else:
    print(df)
    exit(1)


