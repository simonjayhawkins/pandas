# BUG: .equals method returns true when comparing floats with dtype object to None #44190

import numpy as np
import pandas as pd

print(pd.__version__)

left = pd.Series([-np.inf, np.nan, -1.0, 0.0, 1.0, 10 / 3, np.inf], dtype=object)
right = pd.Series([None] * len(left))

print(pd.DataFrame(dict(left=left, right=right)))

print(f"{left.equals(right)=}")

print(f"{right.equals(left)=}")

assert not left.equals(right)
assert not right.equals(left)
