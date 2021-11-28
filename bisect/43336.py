# BUG: Change in index of empty dataframes in mode operation #43336

import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"a": ["a", "b", "a"]}, index=["a", "b", "c"])
result = df.mode(numeric_only=True)
print(result)

expected = pd.DataFrame(index=["a", "b", "c"])
pd.testing.assert_frame_equal(result, expected)
