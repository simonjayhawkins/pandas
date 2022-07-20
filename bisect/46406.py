# BUG: iloc not possible for sparse DataFrame #46406

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([[1.0, 0.0, 1.5], [0.0, 2.0, 0.0]], dtype=pd.SparseDtype(float))
result = df.iloc[0]
print(result)

expected = pd.Series([1.0, 0.0, 1.5], dtype=pd.SparseDtype(float), name=0)
pd.testing.assert_series_equal(result, expected)
