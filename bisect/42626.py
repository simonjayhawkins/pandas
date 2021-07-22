# BUG: Cannot calculate quantiles from Int64Dtype Series when results are floats #42626


import pandas as pd

print(pd.__version__)

result = pd.Series([1, 2, 3], dtype="Int64").quantile(0.75)
print(result)

assert result == 2.5
