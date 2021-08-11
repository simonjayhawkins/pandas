# BUG: TypeError when shifting DataFrame created by concatenation of slices and fills with values #42719

import numpy as np

import pandas as pd

print(pd.__version__)

npa = np.random.RandomState(0).randint(1000, size=(20, 8))
df = pd.DataFrame(npa, columns=[f"c{i}" for i in range(8)])

df1 = df.iloc[:6, 3:5]
df2 = df.iloc[:6, 6:8]
df = pd.concat([df1, df2], axis=1)

result = df.shift(periods=2, axis=1, freq=None, fill_value=0)
print(result)
