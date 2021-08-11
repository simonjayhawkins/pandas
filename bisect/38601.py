import numpy as np

import pandas as pd

print(pd.__version__)

# create a dataframe with non-lexsorted multilevel columns
df = pd.DataFrame(
    np.arange(12).reshape(3, 4),
    columns=pd.MultiIndex.from_tuples([("B", 1), ("B", 2), ("A", "3"), ("A", "4")]),
)

df.loc[:, "A"] = np.zeros(
    (3, 2)
)  # ValueError: Must have equal len keys and value when setting with an ndarray

print(df)
