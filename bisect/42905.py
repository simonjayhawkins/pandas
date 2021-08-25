# BUG: Using agg on a resampled SeriesGroupBy exits Python without traceback #42905

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "class": {
            0: "beta",
            1: "alpha",
            2: "alpha",
            3: "gaga",
            4: "beta",
            5: "gaga",
            6: "beta",
            7: "gaga",
            8: "beta",
            9: "gaga",
            10: "alpha",
            11: "beta",
            12: "alpha",
            13: "gaga",
            14: "alpha",
        },
        "value": {
            0: 69,
            1: 33,
            2: 40,
            3: 2,
            4: 36,
            5: 40,
            6: 48,
            7: 84,
            8: 77,
            9: 22,
            10: 55,
            11: 82,
            12: 37,
            13: 88,
            14: 41,
        },
        "date": {
            0: pd.Timestamp("2021-02-28 00:00:00"),
            1: pd.Timestamp("2021-11-30 00:00:00"),
            2: pd.Timestamp("2021-02-28 00:00:00"),
            3: pd.Timestamp("2021-04-30 00:00:00"),
            4: pd.Timestamp("2021-02-28 00:00:00"),
            5: pd.Timestamp("2021-04-30 00:00:00"),
            6: pd.Timestamp("2021-07-31 00:00:00"),
            7: pd.Timestamp("2021-01-31 00:00:00"),
            8: pd.Timestamp("2021-01-31 00:00:00"),
            9: pd.Timestamp("2021-01-31 00:00:00"),
            10: pd.Timestamp("2021-04-30 00:00:00"),
            11: pd.Timestamp("2021-10-31 00:00:00"),
            12: pd.Timestamp("2021-09-30 00:00:00"),
            13: pd.Timestamp("2021-04-30 00:00:00"),
            14: pd.Timestamp("2021-05-31 00:00:00"),
        },
    }
)

grp = df.set_index("date").groupby("class")
result = grp.resample("M")["value"].agg(["sum", "size"])
print(result)
