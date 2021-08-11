# BUG: numpy functions (eg, np.add) on DataFrames with 'out' parameter no longer work properly #40662

import numpy as np

import pandas as pd

print(pd.__version__)

# doesn't work. bar remains an array of zeros
foo = np.array([1, 2, 3, 4]).reshape(2, 2)
df = pd.DataFrame(foo)
bar = np.zeros_like(df)
print(bar)
result = np.add(df, 1, out=bar)
print(bar)

expected = np.array([[2, 3], [4, 5]])
np.testing.assert_equal(bar, expected)
