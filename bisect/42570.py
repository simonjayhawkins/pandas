# BUG: Less helpful SettingWithCopyWarning on new pandas version #42570

import warnings

import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(np.arange(25).reshape(5, 5))


def valid_indexes(in_df: pd.DataFrame):
    return in_df.loc[:3]


valid = valid_indexes(df)

with warnings.catch_warnings(record=True) as w:
    valid[2] = 3

assert len(w) == 1
assert issubclass(w[0].category, pd.core.common.SettingWithCopyWarning)

result = w[0].filename
expected = __file__
assert result == expected, (result, expected)
