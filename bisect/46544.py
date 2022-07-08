# BUG: DataFrame.loc is not consistent with DataFrame.__setitem__ when used with 2D numpy array #46544

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame(np.zeros((256, 10)))
array_2d = np.zeros((256, 2))

df[0] = array_2d
df.loc[:, 0] = array_2d
