# BUG: The difference in behaviour of indexing between 1.2.4 and 1.3.0 #42461

import pandas as pd

print(pd.__version__)

d = {"col1": [1, 2], "col2": [3, 4]}
df = pd.DataFrame(data=d)
df = df.set_index("col1")

result = df.reset_index()[df.index.names[:]]
print(result)
