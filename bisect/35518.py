import pandas as pd

print(pd.__version__)

df = pd.DataFrame([["orig1", "orig2"]])

tup = ("new1", "new2")

result = df.apply(func=lambda col: tup)
print(result)

expected = pd.Series([tup, tup])

import pandas.testing as tm

tm.assert_series_equal(result, expected)
