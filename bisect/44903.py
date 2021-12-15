# BUG: Boolean type cannot be compared with strigs #44903

import pandas as pd

print(pd.__version__)


s = pd.Series([True, False, pd.NA], dtype="boolean")
try:
    result = s == "X"
except TypeError as e:
    print(e)
    exit(0)
else:
    print(result)
    exit(1)