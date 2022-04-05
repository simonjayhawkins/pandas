# BUG: df.nsmallest get wrong results when row contains NaN #46589

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "a": [1, 2, 3, 4, 5, None, 7],
        "b": [7, 6, 5, 4, 3, 2, 1],
        "c": [1, 1, 2, 2, 3, 3, 3],
    },
    index=np.random.rand(7),
)

result = df.nsmallest(5, columns=["a", "b"])
print(result)

expected = df.iloc[:5]
pd.testing.assert_frame_equal(result, expected)
