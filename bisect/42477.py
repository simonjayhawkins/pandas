# 1.3.0 PerformanceWarning: DataFrame is highly fragmented. #42477

import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"a": np.random.randint(0, 100, size=55), "b": np.random.randint(0, 100, size=55)}
)

# Assign > 100 new columns to the dataframe
for i in range(0, 100):
    df.loc[:, f"n_{i}"] = np.random.randint(0, 100, size=55)
    # Alternative assignment - triggers Performancewarnings here already.
    # df[f'n_{i}'] = np.random.randint(0, 100, size=55)
print(df._data.nblocks)

df1 = df.copy()
result = df1._data.nblocks
assert result == 1, result
