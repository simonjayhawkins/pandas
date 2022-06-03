# BUG: json_normalize generates TypeError: 'NoneType' object is not subscriptable
# as metadata object is not always present. #37783

import pandas as pd

print(pd.__version__)

file = [
    {"values": ["1", "2"], "metadata": {"name": "first_value"}},
    {"values": ["3", "4"], "metadata": None},
]

try:
    df = pd.json_normalize(
        file, record_path="values", meta=[["metadata", "name"]], errors="ignore"
    )
except TypeError as e:
    print(e)
else:
    print(df)
    exit(1)
