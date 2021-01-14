import datetime

import pandas as pd

print(pd.__version__)

assert not pd.NaT < datetime.datetime.now().date()
