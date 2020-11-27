# BUG: Intersection of multiindex returns duplicates #36915

import pandas as pd

print(pd.__version__)

arraysA = [["val1", "val1", "val1", "val1"], ["val2", "val2", "val2", "val2"]]
arraysB = [["val1"], ["val2"]]

indexA = pd.MultiIndex.from_arrays(arraysA, names=("idx1", "idx2"))
indexB = pd.MultiIndex.from_arrays(arraysB, names=("idx1", "idx2"))

res = indexA.intersection(indexB)
print(res)

expected = pd.MultiIndex.from_tuples([("val1", "val2")], names=["idx1", "idx2"])

from pandas import testing as tm

tm.assert_index_equal(res, expected)
