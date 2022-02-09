# BUG: fillna downcast object to int even downcast=False/None #45603

import pandas as pd

print(pd.__version__)

df = pd.Series([1, 2, 3], dtype="object")
result = df.fillna("", downcast=False)  # will get int64 instead
print(result)

assert result.dtype == object
