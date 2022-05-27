# BUG: type error in "mask_missing" method of core/missing.py #47101

import pandas as pd

print(pd.__version__)

# case 1
df = pd.DataFrame({"d": [pd.NA]})
print(df.replace("", pd.NA))
