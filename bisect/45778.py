# BUG: setting with loc breaks in 1.4.0 when indexing using an all-False boolean series #45778

import pandas as pd

print(pd.__version__)

foo = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
bar = pd.Series([6, 7, 8, 9, 10], index=["a", "b", "c", "d", "e"])

# works in 1.3 but breaks in 1.4
foo.loc[foo > 100] = bar
print(foo)
