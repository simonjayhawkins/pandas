import sys
import warnings

import pandas as pd
import pandas._testing as tm

print(pd.__version__)


def f():
    warnings.warn("f1", FutureWarning)
    warnings.warn("f2", RuntimeWarning)


try:
    with tm.assert_produces_warning(None):
        f()
except AssertionError:
    pass
else:
    sys.exit(1)
