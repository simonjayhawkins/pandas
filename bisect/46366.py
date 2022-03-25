# BUG: where method results in a different outputs with "object" and "string" dtypes #46366

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"A": ["1", "", "3"]}, dtype="string")
try:
    result = df.where(df != "", np.nan)
except ValueError as e:
    print(e)
    exit(0)
else:
    print(result)
    exit(1)
