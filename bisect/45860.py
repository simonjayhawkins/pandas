# BUG: Pandas 1.4; df.drop method raises an AttributeError when Int64 index is used and index is not unique #45860

import pandas as pd

print(pd.__version__)


df = pd.DataFrame({"i": pd.Series([1, 2, 2], dtype=pd.Int64Dtype())}).set_index("i")
idx = pd.Index([2])
print(idx)

result = df.drop(idx)  # Raises AttributeError here
print(result)

print(result.index)

# expected = pd.DataFrame([], index=pd.Index([1], dtype="object", name="i"))
# pd.testing.assert_frame_equal(result, expected)
