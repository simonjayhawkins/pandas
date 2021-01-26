import pandas as pd

print(pd.__version__)

d = {"x": [1, 2]}

df1 = pd.DataFrame(data=d, dtype=pd.UInt32Dtype())
df2 = pd.DataFrame(data=d, dtype=pd.UInt32Dtype())

pd.testing.assert_frame_equal(df1, df2, check_exact=True)
