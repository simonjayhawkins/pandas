import pandas as pd
from pandas.tests.extension.decimal import (
    DecimalArray,
    make_data,
)

s = pd.Series(DecimalArray(make_data()[:5]))

print(s)

try:
    s.idxmin()
except TypeError as err:
    msg = "reduction operation 'argmin' not allowed for this dtype"
    assert str(err) == msg
