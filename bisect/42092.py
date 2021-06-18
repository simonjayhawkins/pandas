# BUG?: 1.3.0rc behavior change with concatenating boolean and numeric columns #42092

import pandas as pd

print(pd.__version__)

df1 = pd.DataFrame(pd.Series([True, False, True, True], dtype="bool"))
df2 = pd.DataFrame(pd.Series([1, 0, 1], dtype="int64"))

result = pd.concat([df1, df2])  # dtype changed from int64 to object
print(result)

assert result[0].dtype == "int64", result[0].dtype
