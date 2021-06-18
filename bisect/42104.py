# BUG: DatetimeIndex.intersection gives incorrect result #42104

import pandas as pd

print(pd.__version__)

index = pd.DatetimeIndex(
    [
        "2018-12-31",
        "2019-03-31",
        "2019-06-30",
        "2019-09-30",
        "2019-12-31",
        "2020-03-31",
    ],
    freq="Q-DEC",
)

result = index[::2].intersection(index[1::2])
print(result)

assert not len(result)
