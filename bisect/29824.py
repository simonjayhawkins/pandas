# using to_dict with the 'records' orient produces different results from the default one #29824

import datetime

import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"d": pd.date_range("2018-01-01", freq="12h", periods=2)})
for col in df.select_dtypes(["datetime"]):
    df[col] = pd.Series(df[col].dt.to_pydatetime(), dtype="object")

result = df.to_dict("records")
print(result)

try:
    assert type(result[0]["d"]) is datetime.datetime, type(result[0]["d"])
except AssertionError as err:
    print(err)
else:
    exit(1)

result = df.to_dict("split")
print(result)

try:
    assert type(result["data"][0][0]) is datetime.datetime, type(result["data"][0][0])
except AssertionError as err:
    print(err)
else:
    exit(1)
