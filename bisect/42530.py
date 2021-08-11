# BUG: KeyError when assigning to Series values after pop from DataFrame #42530

import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
s = df.pop("b")
s[[True, False, False]] = 9

print(s)

expected = pd.Series([9, 5, 6], name="b")
pd.testing.assert_series_equal(s, expected)
