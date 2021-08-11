import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    np.random.randn(1000, 3),
    index=pd.date_range("1/1/2012", freq="S", periods=1000),
    columns=[1, "foo", None],
)
r = df.resample("3T")

try:
    r.agg({2: "mean", "bar": "sum"})
except pd.core.base.SpecificationError as err:
    print(err)
    pass
