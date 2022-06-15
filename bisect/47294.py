# BUG: uint16 inserted as int16 when assigning row with dict #47294

import pandas as pd
import numpy as np

print(pd.__version__)

df = pd.DataFrame(columns=["actual", "reference"])
df.loc[0] = {"actual": np.uint16(40_000), "reference": "nope"}

print(df)
print(df.dtypes)

expected = pd.DataFrame(
    {"actual": [np.uint16(40_000)], "reference": ["nope"]}, dtype=object
)
pd.testing.assert_frame_equal(df, expected)
