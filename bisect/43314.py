# BUG: DataFrame.explode is failing on scalar int value. #43314

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        0: [[0, 1, 2], "foo", [], [3, 4]],
        1: 1,
        2: [["a", "b", "c"], np.nan, [], ["d", "e"]],
    }
)

result = df.explode(0)
print(result)
