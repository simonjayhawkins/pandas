# BUG: using dtype='int64' argument of Series causes ValueError: values cannot
# be losslessly cast to int64 for integer strings #44923

import pandas as pd

print(pd.__version__)

result = pd.Series(["1", "2"], dtype="int64")
print(result)
