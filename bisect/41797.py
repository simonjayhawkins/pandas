import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(["a", "b", np.nan])

expected = df.astype(str)

result = df.astype("category").astype(str)
print(result)

pd.testing.assert_frame_equal(result, expected)
