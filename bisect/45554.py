# BUG: Parameter check_flags is ignored in assert_frame_equal #45554

import pandas as pd

print(pd.__version__)

import pandas._testing as tm

df1 = pd.DataFrame([[1, 2], [3, 4]])
df1.flags.allows_duplicate_labels = False
df2 = pd.DataFrame([[1, 2], [3, 4]])
df2.flags.allows_duplicate_labels = True

tm.assert_frame_equal(df1, df2, check_flags=False)
