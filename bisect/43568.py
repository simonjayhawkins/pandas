# REGR: change in output of groupby.apply in 1.3.2 -> 1.3.3 #43568

import pandas as pd

print(pd.__version__)

df = pd._testing.makeTimeDataFrame()

result = df.groupby(df.index.month).apply(lambda x: x.drop_duplicates())
print(result)

assert isinstance(result.index, pd.MultiIndex)
