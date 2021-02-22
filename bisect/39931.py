# BUG: Index alignment behaviour #39931

import numpy as np

import pandas as pd
import pandas.testing as tm

print(pd.__version__)

np.random.seed(1)
df = pd.DataFrame(np.random.randint(0, 100, (10, 2)), columns=["A", "B"])

mask = df["A"] >= 40

df2 = df.copy()

df2[mask] = df[mask].sort_values("A")
print(df2[mask])


tm.assert_frame_equal(df, df2)
