# BUG?: 1.3 behavior change with groupby, apply and side effect #41999

import pandas as pd

print(pd.__version__)


def apply_func(df):
    del df["MEMBER_ID"]

    return df.head(1)


df = pd.DataFrame.from_dict(
    {
        "MONTH": {0: "April", 1: "April", 2: "April"},
        "MEMBER_ID": {0: "Member A", 1: "Member A", 2: "Member B"},
        "ACTIVITY_CATEGORY": {
            0: "Activity 1",
            1: "Days off at homebase",
            2: "Activity 1",
        },
        "FTE": {0: 1.0, 1: 1.0, 2: 0.75},
        "FTE_OFF_DAYS": {0: 5, 1: 5, 2: 10},
    }
)
grp = df.groupby(["MONTH", "FTE"], observed=True)[
    ["MEMBER_ID", "FTE_OFF_DAYS", "ACTIVITY_CATEGORY"]
]
try:
    result = grp.apply(apply_func)
except KeyError as e:
    print(e)
    exit(0)

print(result)

expected = pd.DataFrame(
    {"FTE_OFF_DAYS": [10, 5], "ACTIVITY_CATEGORY": ["Activity 1"] * 2},
    pd.MultiIndex.from_tuples(
        [("April", 0.75, 2), ("April", 1.0, 0)], names=["MONTH", "FTE", None]
    ),
)


pd.testing.assert_frame_equal(result, expected)
exit(1)
