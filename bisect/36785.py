import pandas as pd

pd.__version__

df = pd.DataFrame({"A": [pd.to_datetime("20130101", utc=True)]})
print(df)


def func(x):
    print(x)
    return x


res = df.apply(func, axis=1)
print(res)
