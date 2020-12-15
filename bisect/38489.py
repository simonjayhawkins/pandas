import io
import sys

import pandas as pd

print(pd.__version__)


s = """some_header
2020-01-01 01:00:00"""


try:
    result = pd.read_csv(io.StringIO(s), parse_dates=[], engine="c", delimiter=" ")
    print(result)
except:
    pass
else:
    sys.exit(1)
