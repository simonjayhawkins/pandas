import numpy as np

import pandas as pd

print(pd.__version__)

data = df = pd.DataFrame(
    {
        "a_str": ["A1", "A2", "A3"],
        "b_int": ["1,000", "200", "3"],
        "c_str": ["C1", "C2", "C3"],
        "d_date": ["2021-01-01", "", "2021-03-03"],
    }
)
non_string_columns = ["b_int", "d_date"]

df[non_string_columns] = df[non_string_columns].replace(regex={"": np.nan, ",": ""})

print(df)
