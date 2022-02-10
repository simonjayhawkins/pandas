# BUG: Replacing pd.NA by None has no effect #45601

import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"value": [42, None]}).astype({"value": "Int64"})

result = df.replace({pd.NA: None})
print(result)

expected = pd.DataFrame({"value": [42, None]}, dtype=object)
pd.testing.assert_frame_equal(result, expected)
