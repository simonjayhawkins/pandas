# BUG: replace method with np.nan produces incorrect results #46306

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"A": [0, 1, 2], "B": [1, 0, 2]})
result = df.replace({0: 1, 1: np.nan})
print(result)

expected = pd.DataFrame({"A": [1.0, np.nan, 2.0], "B": [np.nan, 1.0, 2.0]})
pd.testing.assert_frame_equal(result, expected)
