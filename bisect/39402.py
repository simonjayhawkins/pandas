import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(data={"column1": [2.0, -1.0, 3.0]})
df.column1 = df.column1.astype("category")
df.column1 = df.column1.astype(np.int32)
print(df)

print(df.dtypes)

assert df.column1.dtype.type == np.int32  # fails in pandas 1.2.x, returns np.int64
