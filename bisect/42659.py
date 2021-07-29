# BUG:dataframe.groupby('some_column').timedelta.sum() results wrong when timedelta contains NaT (pandas=1.3.0) #42659

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "id": ["1624477460271-3908654213", "1624477460271-3908654213"],
        "dt": [np.nan, pd.to_timedelta("0:0:2")],
    }
)
result = df.groupby("id").dt.sum()
print(result)

expected = pd.Series(
    [pd.to_timedelta("0:0:2")],
    index=pd.Index(["1624477460271-3908654213"], name="id"),
    name="dt",
)
pd.testing.assert_series_equal(result, expected)
