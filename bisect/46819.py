# BUG: Timedelta.total_seconds method is returning wrong values in nanosecond intervals #46819


import numpy as np
import pandas as pd

print(pd.__version__)

duration, Ts = 0.5, 5e-7
signal = pd.to_timedelta(np.arange(0, duration, Ts), "s")

dt = signal[1] - signal[0]

result = dt.total_seconds()
print(result)  # = 5e-07


assert result == 5e-07
