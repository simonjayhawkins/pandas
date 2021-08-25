# Combination of groupby with dropna set to True and apply function not returning expected output #43205

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"a": [1, 2, 3, 4, 5, 6, 7, 8, 9], "b": [1, np.nan, 1, np.nan, 2, 1, 2, np.nan, 1]}
)

df_again = df.groupby("b", dropna=False).apply(lambda x: x)
print(df_again)

pd.testing.assert_frame_equal(df, df_again)
