import datetime as dt

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([[dt.date(2021, 1, 1), 1, "a"], [dt.date(2021, 1, 2), 2, "b"]])

g = df.groupby([0, 1])
print(g.groups.keys())

result = next(iter(key[0] for key in g.groups.keys()))
result

assert isinstance(result, pd.Timestamp)
