# BUG: Pandas 1.4.0 - pd.NaT can not be replaced. #45836

import numpy as np
import pandas as pd

print(pd.__version__)

df = pd.DataFrame([pd.NaT, pd.NaT])
result = df.replace({pd.NaT: None, np.NaN: None})
print(result)
# Either pd.NaT or pd.np.NaN work in 1.3.5

expected = pd.DataFrame([None, None])

pd.testing.assert_frame_equal(result, expected)

