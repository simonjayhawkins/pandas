import pandas as pd


def test_35465():

    # BUG: Inconsistent initialization of timedelta64 between Series vs numpy &
    # pd.TimeDelta #35465

    result = pd.Series([1000000, 200000, 3000000], dtype="timedelta64[s]")

    result[0] == pd.Timedelta("0 days 00:00:00.001000")
    result[1] == pd.Timedelta("0 days 00:00:00.000200")
    result[2] == pd.Timedelta("0 days 00:00:00.003000")
