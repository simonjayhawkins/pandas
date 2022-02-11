# BUG: Type error in groupby.transform(interpolate) #45802

import numpy as np
import pandas as pd

np.random.seed(500)
test_df = pd.DataFrame(
    {
        "a": np.random.randint(low=0, high=1000, size=10000),
        "b": np.random.choice(
            [1, 2, 4, 7, np.nan], size=10000, p=([0.2475] * 4 + [0.01])
        ),
    }
)
grp = test_df.groupby("a")

result = grp.transform(pd.DataFrame.interpolate)
print(result)
