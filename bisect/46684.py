# BUG: apply on DataFrame results in TypeError: copy() missing 1 required positional argument: 'self' #46684

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(list(range(100)))

result = df.apply(lambda x: type(x))
print(result)
