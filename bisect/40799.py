# BUG: behavior change in dataframe.shift(, freq=infer) when upgrading from
# pandas 1.1.5 to 1.2.x #40799

import io

import numpy as np

import pandas as pd

print(pd.__version__)

# replicate the typical data I am reading with pd.rea_csv
dates = np.arange(0, 600.1, 0.1)
dateString = "time, count\n"
for count, time in enumerate(dates):
    dateString = dateString + f"{time:0.3f}, {count}\n"


# create dataframe and convert 'time' as a datetime and put it to index.
df = pd.read_csv(io.BytesIO(dateString.encode()), sep=",")
df["date"] = pd.to_datetime(df.time, unit="s")
df.set_index("date", inplace=True, drop=False)
print(df)

df.shift(
    1, freq="infer"
)  # <-- this is working with pandas 1.1.5 but not any more with 1.2.0 and above
print(df)
