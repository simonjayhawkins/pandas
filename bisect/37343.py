import pandas as pd

print(pd.__version__)


class SubclassedDataFrame2(pd.DataFrame):

    # temporary properties
    _internal_names = pd.DataFrame._internal_names + ["internal_cache"]
    _internal_names_set = set(_internal_names)

    # normal properties
    _metadata = ["added_property"]

    @property
    def _constructor(self):
        return SubclassedDataFrame2


df = SubclassedDataFrame2({"A": [1, 2, 3], "B": [1, 1, 2], "C": [7, 8, 9]})
df.added_property = "hello"
for i, d in df.groupby("B"):
    assert d.added_property == "hello"
