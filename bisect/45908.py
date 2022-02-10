# BUG: DataFrame.first has unexpected behavior when passing a DateOffset #45908

import numpy as np
import pandas as pd

print(pd.__version__)

i = index = pd.date_range("2018-04-09", periods=30, freq="2D")
df = pd.DataFrame({"A": pd.Series(np.arange(30), index=i)}, index=i)
do = pd.DateOffset(days=15)

result = df.first(do)
print(result)

expected = df.first("15D")
pd.testing.assert_frame_equal(result, expected)
