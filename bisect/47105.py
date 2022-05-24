# BUG: nan comparisons behave differently on identical objects #47105

import numpy as np
import pandas as pd

print(pd.__version__)

idx = pd.Index([np.nan])
result = idx > idx
print(result)

expected = np.array([False])
pd._testing.assert_numpy_array_equal(result, expected)
