# df.duplicated and drop_duplicates raise TypeError with set and list values. #12693

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([[{"a", "b"}], [{"b", "c"}], [{"b", "a"}]])

try:
    result = df.duplicated()
except TypeError as e:
    print(e)
else:
    print(result)
    exit(1)
