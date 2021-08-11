import numpy as np

import pandas as pd

df = pd.DataFrame(
    [
        ["A", "group_1", pd.Timestamp(2019, 1, 1, 9)],
        ["B", "group_1", pd.Timestamp(2019, 1, 2, 9)],
        ["C", "group_2", pd.Timestamp(2019, 1, 3, 9)],
        ["D", "group_1", pd.Timestamp(2019, 1, 6, 9)],
        ["E", "group_1", pd.Timestamp(2019, 1, 7, 9)],
        ["F", "group_1", pd.Timestamp(2019, 1, 10, 9)],
        ["G", "group_2", pd.Timestamp(2019, 1, 20, 9)],
        ["H", "group_1", pd.Timestamp(2019, 4, 8, 9)],
    ],
    columns=["index", "group", "eventTime"],
).set_index("index")

groups = df.groupby("group")
df["count_to_date"] = groups.cumcount()
rolling_groups = groups.rolling("10d", on="eventTime")
group_size = rolling_groups.apply(lambda df: df.shape[0])
print(group_size)

index = pd.MultiIndex.from_tuples(
    [
        ("group_1", "A"),
        ("group_1", "B"),
        ("group_1", "D"),
        ("group_1", "E"),
        ("group_1", "F"),
        ("group_1", "H"),
        ("group_2", "C"),
        ("group_2", "G"),
    ],
    names=["group", "index"],
)

columns = pd.Index(["eventTime", "count_to_date"], dtype="object")

values = np.array(
    [
        [pd.Timestamp("2019-01-01 09:00:00"), 1.0],
        [pd.Timestamp("2019-01-02 09:00:00"), 2.0],
        [pd.Timestamp("2019-01-06 09:00:00"), 3.0],
        [pd.Timestamp("2019-01-07 09:00:00"), 4.0],
        [pd.Timestamp("2019-01-10 09:00:00"), 5.0],
        [pd.Timestamp("2019-04-08 09:00:00"), 1.0],
        [pd.Timestamp("2019-01-03 09:00:00"), 1.0],
        [pd.Timestamp("2019-01-20 09:00:00"), 1.0],
    ],
    dtype=object,
)

expected = pd.DataFrame(values, index=index, columns=columns)
expected.count_to_date = expected.count_to_date.astype("float")

import pandas.testing as tm

tm.assert_frame_equal(group_size, expected)
