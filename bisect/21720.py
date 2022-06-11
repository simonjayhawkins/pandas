# BUG: df.duplicated treats None as np.nan in object columns #21720

import numpy as np
import pandas as pd

print(pd.__version__)

s = pd.Series([np.nan, 3, 3, None, np.nan], dtype=object)
result = s.to_frame().duplicated()
print(result)

expected = pd.Series([0, 0, 1, 1, 1], dtype=bool)
pd.testing.assert_series_equal(result, expected)
