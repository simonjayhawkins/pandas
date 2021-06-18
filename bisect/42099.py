# BUG: Adding Series to empty DataFrame can reset dtype to float64 #42099

import pandas as pd

print(pd.__version__)

data = pd.array([0, 1, 2, 3], dtype="Int32")
df = pd.DataFrame({"data": pd.Series(data)})

result = pd.DataFrame(index=df.index)

result.loc[df.index, "data"] = df["data"]

expected_dtype = df["data"].dtype
dtype = result["data"].dtype

print(dtype)  # prints: float64 <--

assert dtype == expected_dtype
