# BUG: Regression on SeriesGrouper using Timestamp index with pandas 1.3.0 #42390

import numpy as np
import pandas as pd

print(pd.__version__)

def agg(series):
    if series.isna().values.all():
        return None
    return np.sum(series)


df = pd.DataFrame([1.0], index=[pd.Timestamp("2018-01-16 00:00:00+00:00")])

result = df.groupby(lambda x: 1).agg(agg)
print(result)

expected = pd.DataFrame([1.0], index=[1])
pd.testing.assert_frame_equal(result, expected)

