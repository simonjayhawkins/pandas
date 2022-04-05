# BUG: Unexpected jupyter notebook behavior when assigning an array.array variable #46268

from array import array

import numpy as np

import pandas as pd

print(pd.__version__)


df = pd.DataFrame({"A": [2, 4, 6, 8]})

cenlon = array("d")
cenlon.append(45.345343)

# Problem
df.loc[0, "CenLon"] = cenlon
print(df)

expected = pd.DataFrame(
    {"A": [2, 4, 6, 8], "CenLon": [45.345343, np.nan, np.nan, np.nan]}
)
pd.testing.assert_frame_equal(df, expected)
