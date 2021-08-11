# BUG: astype() on an integer DataFrame changes the order of data #42396

import numpy as np

import pandas as pd

print(pd.__version__)

npa = np.random.RandomState(0).randint(1000, size=(20, 8))
df = pd.DataFrame(npa, columns=[f"c{i}" for i in range(8)]).iloc[:6, :3]
result = df.astype("int32")
print(result)

pd.testing.assert_frame_equal(result, df, check_dtype=False)
