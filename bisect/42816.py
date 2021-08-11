# BUG: nlargest raises TypeError "No matching signature found" on Float64Dtype Series, versions >1.3.0 #42816

import numpy as np

import pandas as pd

print(pd.__version__)

s = pd.Series(np.random.random(10)).astype("Float64")

result = s.nlargest(5)
print(result)
