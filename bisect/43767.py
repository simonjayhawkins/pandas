# BUG: reset_index after a group_by raise a ValueError for empty dataframe #43767

import datetime as dt

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([(dt.date.today(), "b", 12)], columns=["date", "b", "count"])
df["date"] = pd.to_datetime(df["date"])
df = df[
    df["count"] == 1
]  # uncomment this line to make the dataframe empty and so reset_index raising an exception
result = df.set_index("date").groupby(["b"]).resample("M").sum().reset_index()
print(result)
