import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(["o", "o'doul's", "oad", "oaf", "oafish"])
df = df.astype("|S")
print(df)

print(df.dtypes)

df.replace({None: np.nan})
