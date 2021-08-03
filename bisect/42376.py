# BUG: 1.3.0 column assignment via single columnnp.matrix behaviour change #42376

import numpy as np
from scipy import sparse

import pandas as pd

print(pd.__version__)


X = sparse.random(100, 100, density=0.2, format="csr")
df = pd.DataFrame({"a": np.arange(100)})
df["X_sum"] = X.sum(axis=1)
print(df)
