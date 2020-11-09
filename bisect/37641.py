import pandas as pd

print(pd.__version__)


arrays = [["val1", "val1", "val2"], ["val1", "val1", "val2"]]
index = pd.MultiIndex.from_arrays(arrays, names=("idx1", "idx2"))

s = pd.Series([1, 2, 3], index=index)

res = s.groupby(["idx1", "idx2"], group_keys=False).rolling(1).mean()
print(res)

mi = pd.MultiIndex.from_tuples(
    [("val1", "val1"), ("val1", "val1"), ("val2", "val2")], names=["idx1", "idx2"]
)

import pandas.testing as tm

tm.assert_index_equal(res.index, mi)
