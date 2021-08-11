import numpy as np

import pandas as pd

print(pd.__version__)

g = np.random.default_rng(840812492384587325982704)
a = pd.Series(g.integers(0, 3, size=100)).astype("category")
b = pd.Series(g.integers(0, 2, size=100)).astype("category")
res = pd.crosstab(a, b, margins=True, dropna=False)
print(res)
