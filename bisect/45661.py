# BUG: join operation fails on overlapping IntervalIndex levels #45661

import pandas as pd

print(pd.__version__)

range_index = pd.RangeIndex(3, name="range_index")
interval_index = pd.IntervalIndex.from_tuples(
    [(0.0, 1.0), (1.0, 2.0), (1.5, 2.5)], name="interval_index"
)
multi_index = pd.MultiIndex.from_product([interval_index, range_index])

result = interval_index.join(multi_index)
print(result)

pd.testing.assert_index_equal(result, multi_index)

# This causes the same issue
result = multi_index.join(interval_index)
print(result)

pd.testing.assert_index_equal(result, multi_index)
