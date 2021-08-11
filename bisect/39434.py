import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(np.arange(64))
length = len(df.index)
df.index = [(i - length / 2) % length for i in range(length)]
result = df.sort_index(axis=0, ascending=None, na_position="first")
print(result)
