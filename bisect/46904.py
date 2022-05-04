# BUG: aggregate function on transposed resampled data frame raises ValueError #46904

import pandas as pd

print(pd.__version__)

DIM = 3
now = pd.Timestamp.now()
# Create data frame.
data = [[i + j for i in range(DIM)] for j in range(DIM)]
columns = [now + pd.DateOffset(i) for i in range(DIM)]
df = pd.DataFrame(data=data, columns=columns)

# Calculate mean/min/max/sum per month.
try:
    df.resample("M", axis=1).aggregate(["mean", "min", "max", "sum"])
except NotImplementedError as e:
    print(e)
