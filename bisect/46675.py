# Index is being materialized in pd.concat when axis=1 #46675

import pandas as pd

print(pd.__version__)

s1 = pd.Series(["a", "b", "c"])
s2 = pd.Series(["a", "b"])
s3 = pd.Series(["a", "b", "c", "d"])
s4 = pd.Series([])
# <stdin>:1: FutureWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.

sort = False
join = "outer"
ignore_index = False
axis = 1

result = pd.concat(
    [s1, s2, s3, s4],
    sort=sort,
    join=join,
    ignore_index=ignore_index,
    axis=axis,
)

print(result.index)

assert isinstance(result.index, pd.RangeIndex)
