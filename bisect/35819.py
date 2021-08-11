import pandas as pd

print(pd.__version__)

data = {
    "number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    "name": [
        "foo1",
        "foo2",
        "foo3",
        "foo4",
        "foo5",
        "foo6",
        "foo7",
        "foo8",
        "foo9",
        "foo0",
    ],
}

ser = pd.DataFrame(
    data,
    index=pd.DatetimeIndex(
        [
            "2020-07-22 11:47:42",
            "2020-07-23 07:58:50",
            "2020-07-26 05:39:43",
            "2020-07-27 05:41:12",
            "2020-07-28 08:52:34",
            "2020-07-29 11:01:01",
            "2020-07-01 00:20:08",
            "2020-06-30 10:05:04",
            "2020-07-02 09:50:04",
            "2020-07-03 09:50:05",
        ]
    ),
    columns=["number", "name"],
)

res = ser["20200701":]
print(res)
