# BUG: "replace" does not work with different numpy-int types even when values are the same #45311

import numpy as np
import pandas as pd

print(pd.__version__)

maps = pd.Series(
    [np.int64(0), np.int64(2), np.int64(1)]
)  # index-value should be mapped to series-value
map_dict = {old: new for (old, new) in zip(maps.values, maps.index)}

labs = pd.Series([1, 1, 1, 0, 0, 2, 2, 2]).astype(
    np.int32
)  # Simulate a list of observations

result = labs.replace(map_dict)
print(result)

# test against old incorrect behaviour to find commit that fixes
pd.testing.assert_series_equal(result, labs)
