import pandas as pd

print(pd.__version__)

df = pd.DataFrame([[10.1]], columns=pd.DatetimeIndex(["8/21/2020 12:00:00 AM"]))
key = df.columns[0].date()

res = df[key]
print(res)
