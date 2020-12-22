import sys

import numpy as np

import pandas as pd
import pandas.testing as tm

print(pd.__version__)

data = np.broadcast_to(np.arange(2)[None, :], (3, 2))

df_sorted = pd.DataFrame(
    data, columns=pd.MultiIndex.from_product([["level_0"], ["a", "b"]]), dtype=int
)

df_unsorted = df_sorted.reindex(
    pd.MultiIndex.from_product([["level_0"], ["b", "a"]]), axis=1
)

result = df_unsorted.loc[:, ("level_0", ["a", "b"])]
print(result)

expected = pd.DataFrame(
    data, columns=pd.MultiIndex.from_product([["level_0"], ["a", "b"]])
)


try:
    tm.assert_frame_equal(result, expected)
except AssertionError:
    pass
else:
    sys.exit(1)
