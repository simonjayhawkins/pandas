# REGR: assignment of pd.NA with enlargement gives object dtype with IntegerArray #47284

import pandas as pd

print(pd.__version__)

# gets upcast to object
df = pd.DataFrame({"a": [1, 2, 3]}, dtype="Int64")
df.loc[4] = pd.NA
print(df.dtypes)

expected = pd.DataFrame(
    {"a": [1, 2, 3, None]},
    dtype="Int64",
    index=pd.Int64Index([0, 1, 2, 4], dtype="int64"),
)
pd.testing.assert_frame_equal(df, expected)
