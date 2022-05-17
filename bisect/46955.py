# BUG: index_col=False doesn't work for unequal length of data #46955

from io import StringIO

import pandas as pd

print(pd.__version__)


TESTDATA = StringIO(
    """
0.5 0.03
0.1  0.2  0.3   2
0.2  0.1     0.1  0.3
0.5 0.03
0.1  0.2   0.3      2
    """
)

df = pd.read_csv(TESTDATA, sep=" +", header=None, index_col=False, engine="python")

print(df)

expected = pd.DataFrame({0: [0.5, 0.1, 0.2, 0.5, 0.1], 1: [0.03, 0.2, 0.1, 0.03, 0.2]})
pd.testing.assert_frame_equal(df, expected)
