import pandas as pd

print(pd.__version__)

foo = pd.DataFrame(
    {
        "some_string": ["612092d7-071f-467e832d-dd53e0f2b590-0006"],
        "time": [pd.NaT],
    }
)

try:
    result = list(foo.iterrows())
    print(result)
    assert False
except OverflowError as e:
    print(e)
