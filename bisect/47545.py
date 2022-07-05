# BUG: datetime index name droped after date_range selection #47545

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "date": [pd.to_datetime(d) for d in ["20220101", "20220102", "20220103"]],
        "value": [1, 2, 3],
    }
).set_index("date")

result = df.loc[pd.date_range("20220101", "20220102"), :]
print(result)

assert result.index.name == "date"
