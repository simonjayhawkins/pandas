# BUG: Series.groupby fails with InvalidIndexError on time series with a tuple-named grouper. #42731

import pandas as pd

print(pd.__version__)

s = pd.Series(index=[pd.Timestamp(2021, 7, 26)], name=("A", 1))

result = s.groupby(s==s)  # raises InvalidIndexError
print(result)
