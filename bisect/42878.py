# BUG: [float32 precision] pandas float32 mean is inconsistent with numpy #42878

import numpy as np

import pandas as pd

print(pd.__version__)

a = pd.Series(np.random.normal(scale=0.1, size=(1_000_000,)).astype(np.float32)).pow(2)

result = np.mean(a)
print(result, type(result))

expected = np.mean(a.values)
assert isinstance(result, np.float32)
assert isinstance(expected, np.float32)
assert result == expected
