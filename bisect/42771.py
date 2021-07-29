# BUG: DataFrame.drop() can't drop row by index tuple when MultiIndex has duplicated value in a level. #42771

import pandas as pd

print(pd.__version__)

lev_0 = [1, 2]
lev_1 = [1, 1]
idx = pd.MultiIndex.from_product([lev_0, lev_1])
df = pd.DataFrame(data={"a": range(0, len(idx))}, index=idx)

result = df.drop(index=df.index[0])
print(result)

expected = df.iloc[-2:]
pd.testing.assert_frame_equal(result, expected)
