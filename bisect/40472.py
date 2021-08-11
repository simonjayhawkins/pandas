# BUG: series.replace(np.nan,..) on categorical series does not replace #40472


import numpy as np

import pandas as pd

print(pd.__version__)

s = pd.Series({1: np.nan, 2: "b"}).astype("category")
result = s.replace(np.nan, "c")
print(result)

assert result[1] == "c"
