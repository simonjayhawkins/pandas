# BUG: inconsistent groupby.apply behaviour depending on column dtypes #43206

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "date_val": {
            0: pd.Timestamp("2017-01-01 00:00:00"),
            1: pd.Timestamp("2017-01-01 00:00:00"),
            2: pd.Timestamp("2017-02-01 00:00:00"),
            3: pd.Timestamp("2017-02-01 00:00:00"),
        },
        "uid": {0: "1", 1: "2", 2: "1", 3: "2"},
        "str_val": {
            0: str("2017-01-01 00:00:00"),
            1: str("2017-01-01 00:00:00"),
            2: str("2017-02-01 00:00:00"),
            3: str("2017-02-01 00:00:00"),
        },
    }
)

# df1 = df.groupby("uid", as_index=False)[["uid", "str_val", "date_val"]].apply(
#     lambda x: x.sort_values(by="str_val", ascending=True)
# )
# print(df1)

df2 = df.groupby("uid", as_index=False)[["uid", "str_val"]].apply(
    lambda x: x.sort_values(by="str_val", ascending=True)
)
print(df2)

expected = pd.MultiIndex.from_tuples(
    [(0, 0), (0, 2), (1, 1), (1, 3)],
)
pd.testing.assert_index_equal(df2.index, expected)
