# BUG: Series.replace converts np.nan into pd.NaT implicitly #48034

import numpy as np
import pandas as pd

print(pd.__version__)

s1 = pd.Series([pd.Timestamp(1000223), np.nan], dtype=object)

result = s1.replace("abcdef", pd.NaT, regex=True)
print(result)

pd.testing.assert_series_equal(result, s1)
