# BUG: MultiIndex.dtypes index behavior changes after 1.4.x #46900

import pandas as pd

print(pd.__version__)

arrays = [[1, 1, 2, 2], ["red", "blue", "red", "blue"]]
pmidx = pd.MultiIndex.from_arrays(arrays, names=[("zero", "first"), ("one", "second")])

result = pmidx.dtypes.index
print(result)

expected = pd.MultiIndex.from_tuples(
    [("zero", "first"), ("one", "second")],
)
pd.testing.assert_index_equal(result, expected)
