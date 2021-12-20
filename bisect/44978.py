# BUG: shift with large periods creates mulfunctioning dtypes with master branch #44978

import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(np.random.rand(5, 3))
result = df.shift(6, axis=1, fill_value=None)

print(result)

expected = pd.DataFrame(np.full((5, 3), np.nan))

pd.testing.assert_frame_equal(result, expected)
