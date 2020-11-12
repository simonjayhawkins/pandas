import pandas as pd

print(pd.__version__)

s = pd.Series(
    [1, 2, 3], index=pd.MultiIndex.from_tuples([("a", "A"), ("b", "B"), ("c", "C")])
)
df = s.to_frame()
print(
    s.loc[
        ("a",),
    ]
)
print(
    df.loc[
        ("a",),
    ]
)

df.loc[
    ("a",),
] = 0

print(df)
