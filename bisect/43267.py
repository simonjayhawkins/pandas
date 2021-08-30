# BUG: crash in df.groupby.rolling.mean with forward window indexer #43267

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"B": [np.nan, 1, 2, np.nan, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}
)
df["A"] = 1
indexer = pd.api.indexers.FixedForwardWindowIndexer(window_size=12)  # forward 12 period

# First time is OK
df["mean"] = (
    df.groupby("A")["B"]
    .rolling(window=indexer, min_periods=1)
    .mean()
    .reset_index()
    .loc[:, "B"]
)

# Second time would crash!
df["mean"] = (
    df.groupby("A")["B"]
    .rolling(window=indexer, min_periods=1)
    .mean()
    .reset_index()
    .loc[:, "B"]
)
print(df)
