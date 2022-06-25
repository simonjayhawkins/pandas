# BUG: NotImplementedError: Prefix not defined when slicing offset with loc #46671

import numpy as np
import pandas as pd

print(pd.__version__)

d = pd.DataFrame(np.random.rand(10, 1))
d.set_index(pd.date_range("01-01-2022", periods=10), inplace=True)
d = d.asfreq(pd.DateOffset(days=1))
result = d.loc["2022-01-01":"2022-01-03"]
print(result)
