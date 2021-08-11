import numpy as np

import pandas as pd

print(pd.__version__)

increment = pd.Series(pd.to_timedelta(30 + np.random.randn(1000), unit="s")).cumsum()
increment[-1] = None
index = pd.Timestamp("2012-01-01 09:00") + increment
df = pd.Series(range(len(index)), index=index).to_frame()
print(df)

res = df["2012-01-01":"2012-01-05"]
print(res)
