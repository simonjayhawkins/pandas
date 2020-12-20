import pandas as pd

print(pd.__version__)

foo = pd.DataFrame(
    {
        "some_string": ["612092d7-071f-467e832d-dd53e0f2b590-0006"],
        "time": [pd.NaT],
    }
)

result = list(foo.iterrows())
print(result)
