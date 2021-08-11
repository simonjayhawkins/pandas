import numpy as np

import pandas as pd

pd.__version__


result = (
    pd.DataFrame({"foo": [2, 1], "bar": [2, 1]})
    .groupby("foo", sort=False)
    .rolling(1)
    .min()
)
print(result)

values = np.array([[2.0, 2.0], [1.0, 1.0]])

columns = pd.Index(["foo", "bar"], dtype="object")

index = pd.MultiIndex.from_tuples([(2, 0), (1, 1)], names=["foo", None])


expected = pd.DataFrame(values, index=index, columns=columns)


import pandas.testing as tm

tm.assert_frame_equal(result, expected)
