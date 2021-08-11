# BUG: Regression on DataFrame.from_records #42456

from numpy import (
    array,
    empty,
)

import pandas as pd

print(pd.__version__)

structured_dtype = [("prop", int)]

# Does NOT work any more
result = empty((0, len(structured_dtype)))
structured_array = array(result, dtype=structured_dtype)
result = pd.DataFrame.from_records(structured_array)
print(result)
