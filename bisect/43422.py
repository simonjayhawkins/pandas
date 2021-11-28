# BUG: Regression in 1.3.0: Exception when setting arrays as cell values #43422

from numpy import zeros

import pandas as pd
from pandas import DataFrame

print(pd.__version__)

# (Leaving out the dtype doesn't change things)
frame = DataFrame(columns=["x", "P"], dtype=object)
data = {"x": zeros((2,)), "P": zeros((2, 2))}
expected = frame.append(data, ignore_index=True)

frame.loc[0] = data
print(frame)

pd.testing.assert_frame_equal(frame, expected)
