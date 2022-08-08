# BUG: Setting a DataFrame as rhs with loc on a single column does not align in the single
# block case #47578

import numpy as np
import pandas as pd

print(pd.__version__)

result = pd.DataFrame({"var": [1, 2]}, index=[1, 2])
rhs = pd.DataFrame({"var": [10, 11]}, index=[2, 3])
result.loc[:, "var"] = rhs
print(result)

expected = pd.DataFrame({"var": [np.nan, 10]}, index=[1, 2])
try:
    pd.testing.assert_frame_equal(result, expected)
except AssertionError as e:
    print(e)
else:
    exit(1)
