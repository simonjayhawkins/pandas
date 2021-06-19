# BUG: 1.3.0rc Series.mode errors with BooleanDtype series containing nans #42107

import pandas as pd

print(pd.__version__)


s = pd.Series([True, False, True, pd.NA], dtype="boolean")

result = s.mode()
print(result)

expected = pd.Series([True], dtype="boolean")

pd.testing.assert_series_equal(result, expected)
