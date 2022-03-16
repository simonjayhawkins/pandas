# BUG: RecursionError when attempting to replace np.nan values under main branch #45725


import numpy as np

import pandas as pd

print(pd.__version__)

NaN_values = [np.nan, np.nan]
ser = pd.Series(data=NaN_values)
df = pd.DataFrame(data=NaN_values)


ser = ser.replace({np.nan: pd.NA})
print(ser)

df = df.replace({np.nan: None})
print(df)
