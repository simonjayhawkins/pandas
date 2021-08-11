# BUG: Change in behavior of replace with integer series and float to_replace
# #40371

import numpy as np

import pandas as pd

print(pd.__version__)

result = pd.Series([1]).replace(np.array([1.0]), [0])
print(result)

expected = pd.Series([0])
pd.testing.assert_series_equal(result, expected)
