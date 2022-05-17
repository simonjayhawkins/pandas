# BUG: DataFrame.shift shows different behavior for axis=1 when freq is specified #47039

import numpy as np
import pandas as pd

print(pd.__version__)

rs = np.random.RandomState(0)

raw = pd.DataFrame(
    rs.randint(1000, size=(10, 8)), columns=["col" + str(i + 1) for i in range(8)]
)
raw.index = pd.date_range("2020-1-1", periods=10)
raw.columns = pd.date_range("2020-3-1", periods=8)
result = raw.shift(periods=2, freq="D", axis=1)
print(result)

expected = raw.shift(periods=2, freq="D", axis=1, fill_value=0)
pd.testing.assert_frame_equal(result, expected)
