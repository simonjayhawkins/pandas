import dask.array as da

import pandas as pd

print(pd.__version__)

a = da.ones((12,), chunks=4)

s = pd.Series(a, index=range(12))
print(s)

assert s.dtype == "float64"
