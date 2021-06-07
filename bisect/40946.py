# BUG: total_seconds() method returns zero for timedeltas smaller then 1 microsecond
# #40946

import pandas as pd

print(pd.__version__)

# create 500ns Timedelta - it is not converted successfully to float - result is zero
b = pd.Timedelta("500ns")
print(b)

result = b.total_seconds()
print(result)

assert result == 5e-07
