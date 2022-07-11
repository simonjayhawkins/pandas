# BUG: Inconsistent handling of dropping levels in MultiIndex when using IndexSlice #47596

import pandas as pd

print(pd.__version__)

idx = pd.IndexSlice
df = pd.DataFrame(
    index=pd.MultiIndex.from_product([["A", "B"], range(2), ["a", "b"]]),
    columns=pd.MultiIndex.from_product([["a", "b"], range(2)]),
)
result = df.loc[idx["A", :, :]]
print(result)

expected = pd.DataFrame(
    index=pd.MultiIndex.from_product([["A"], range(2), ["a", "b"]]),
    columns=pd.MultiIndex.from_product([["a", "b"], range(2)]),
)
pd.testing.assert_frame_equal(result, expected)
