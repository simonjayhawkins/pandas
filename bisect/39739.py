import pandas as pd

print(pd.__version__)

one = pd.Index([], dtype="object")
two = pd.RangeIndex(start=0, stop=0, step=1)
df_one = pd.DataFrame(index=one)
df_two = pd.DataFrame(index=two)
print(df_one)
print(df_two)
pd.testing.assert_frame_equal(df_one, df_two, check_like=True)
