# BUG: 1.4.0rc1 AssertionError when reset_index drops all indexes except for an empty RangeIndex. #45230

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(columns=["brand"], dtype=np.int64, index=pd.RangeIndex(0, 0, 1))
df = df.set_index([df.index, "brand"])

result = df.reset_index([1], drop=True)
print(result)

expected = pd.DataFrame(index=pd.Int64Index([], dtype="int64"))
pd.testing.assert_frame_equal(result, expected)
