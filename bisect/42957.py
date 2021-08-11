# BUG: pd.to_datetime with format doesn't work with pd.NA #42957

import pandas as pd

print(pd.__version__)

a = pd.DataFrame({"a": [pd.NA]})

result = pd.to_datetime(a["a"], format="%Y%m%d%H%M%S")  # -> Error

print(result)
