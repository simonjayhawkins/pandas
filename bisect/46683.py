# BUG: Segmentation fault when JSON serializing a PeriodIndex #46683

import faulthandler

import pandas as pd

faulthandler.enable()

print(pd.__version__)

s = pd.Series(["2022-04-06", "2022-04-07"])
p = pd.PeriodIndex(s, freq="D")
df = pd.DataFrame(index=p)
result = df.to_json()
print(result)
