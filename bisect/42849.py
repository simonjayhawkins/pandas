# BUG: GroupBy's quantile incompatible with pd.NA #42849

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"x": [1, 1], "y": [0.2, np.nan]}).astype(
    {"x": pd.Int64Dtype(), "y": pd.Float64Dtype()}
)

result = df.groupby("x")["y"].quantile(0.5)
print(result)
