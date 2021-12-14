# BUG: inconsistency in dtype of replace() #44864

import pandas as pd

print(pd.__version__)
s = pd.Series(["0"])
res1 = s.replace(to_replace="0", value=1, regex=False)  # shows int64
print(res1)
res2 = s.replace(to_replace="0", value=1, regex=True)  # shows object
print(res2)

assert res2.dtype == "int64"
