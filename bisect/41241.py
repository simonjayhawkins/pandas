# BUG: New param [use_nullable_dtypes] of pd.read_parquet() can't handle empty parquet
# file #41241

import pandas as pd

print(pd.__version__)


df = pd.DataFrame({"value": pd.array([], dtype=pd.Int64Dtype())})
df.to_parquet("test")
try:
    df2 = pd.read_parquet("test")
except ValueError as e:
    print(e)
else:
    print(df2)
    raise AssertionError
