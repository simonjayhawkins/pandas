# BUG: Segfault when printing dataframe #46848

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(np.empty((1, 33), dtype=object))
for col in df.columns:
    df[col] = np.empty_like(df[col])

print(df)
