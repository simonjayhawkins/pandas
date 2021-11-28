# BUG: RangeIndex.where throws AssertionError #43240

import numpy as np

import pandas as pd

print(pd.__version__)

idx = pd.RangeIndex(0, 5)
v = np.array([False, False, True, True, True])

result = idx.where(v, 10)
print(result)

expected = pd.Index([10, 10, 2, 3, 4], dtype="int64")

pd.testing.assert_index_equal(result, expected)
