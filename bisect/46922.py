# BUG: Concatenation of None with numerical values no longer converts None to Nan. #46922

import pandas as pd

print(pd.__version__)

df1 = pd.DataFrame({"A": [None], "B": [12.34]})
df2 = pd.DataFrame({"A": [12.34], "B": [12.34]})

result = pd.concat([df1, df2])
print(result)
print(result.dtypes)

expected = pd.DataFrame(
    {"A": [None, 12.34], "B": [12.34, 12.34]}, dtype=float, index=[0, 0]
)
pd.testing.assert_frame_equal(result, expected)
