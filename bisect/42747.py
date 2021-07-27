# BUG: freq attribute is None after set_index #42747

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"datetime": pd.date_range("1/1/1", periods=20, freq="H", tz="UTC")})
df.set_index("datetime", inplace=True)

result = df.index.freq
print(result)
assert result == "H", result