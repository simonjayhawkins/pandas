# Passing an empty list to read_csv causes segmentation fault #45957

import pandas as pd

print(pd.__version__)

try:
    pd.read_csv([])
except ValueError as err:
    print(err)
    exit(0)
