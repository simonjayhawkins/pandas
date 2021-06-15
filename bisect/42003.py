# BUG: 1.3.0rc1 pd.util.hash_array on Index fails to access _values_for_factorize #42003

import pandas as pd

print(pd.__version__)

index = pd.Index([1, 2, 3])
result = pd.util.hash_array(index)

print(result)
