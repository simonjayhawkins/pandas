# BUG: DatetimeIndex has become unhashable in 1.3.1? #42844

import random

import pandas as pd

print(pd.__version__)

# Right data
ts_open = pd.DatetimeIndex(
    [
        pd.Timestamp("2021/01/01 00:37"),
        pd.Timestamp("2021/01/01 00:40"),
        pd.Timestamp("2021/01/01 01:00"),
        pd.Timestamp("2021/01/01 03:45"),
        pd.Timestamp("2021/01/01 03:59"),
        pd.Timestamp("2021/01/01 05:20"),
    ]
)
length = len(ts_open)
random.seed(1)
volume = random.sample(range(1, length + 1), length)
df_smpl = pd.DataFrame({"volume": volume, "ts_open": ts_open})

# Left data
ts_full = pd.date_range(start=pd.Timestamp("2021/01/01 00:00"), periods=7, freq="1h")
ts_event = ts_full[:-1]
length_ipr = len(ts_event)
random.seed(2)
volume = random.sample(range(20, length_ipr + 20), length_ipr)
df_ipr = pd.DataFrame({"volume": volume, "timestamp": ts_event})

at = ts_full[1:]
df_smpl.index = df_smpl["ts_open"]

# Test
df_full = pd.merge_asof(
    df_ipr,
    df_smpl,
    left_on=at,
    right_index=True,
    allow_exact_matches=False,
    direction="backward",
)

print(df_full)
