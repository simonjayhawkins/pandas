# BUG: 1.4.0 does not preserve initially empty Index and appended by loc assignment. #45621

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(columns=["a", "b"]).set_index("a")
print(df.index, id(df.index))  # Index([], dtype='object', name='a') 4644041536

df.loc[0] = {"b": 0}
result = df.index
print(result, id(df.index))  # Int64Index([0], dtype='int64') 4726025904

expected = pd.Index([0], dtype="int64", name="a")
pd.testing.assert_index_equal(result, expected)
