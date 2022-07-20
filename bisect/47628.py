# BUG: Inconsistent behavior between None and pd.NA #47628

import pandas as pd

print(pd.__version__)

x = pd.Series(
    ["90210", "60018-0123", "10010", "text", "6.7", "<class 'object'>", "123456"],
    dtype="string",
)
invalid = pd.Series([False, False, False, True, True, True, True])
x[invalid] = None
print(x)

print(x._values)

assert x[6] is pd.NA, type(x[6])
