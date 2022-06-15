# BUG: uint64 series resampling #47301

import datetime

import pandas as pd

print(pd.__version__)

period = "15s"
df = pd.DataFrame([["80000000", 1], ["80101000", 100]], columns=["Time", "Value"])
df["DateTime"] = df["Time"].apply(
    lambda s: datetime.datetime.strptime(str(s), "%H%M%S%f")
)
df.set_index("DateTime", inplace=True)
df["Value"] = df["Value"].astype("uint64")

df_rs = df["Value"].resample(period)
try:
    print(df_rs.first())
except RuntimeError as e:
    print(e)
else:
    exit(1)
