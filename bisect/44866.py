# BUG: DataFrame.copy mutates the source dataframe, discarding Series attributes listed in Series._metadata. #44866
"""
Metadata wipeout example.
"""

import pandas as pd

print(pd.__version__)


class S(pd.Series):
    _metadata = ["foo"]

    @property
    def _constructor(self):
        return S

    @property
    def _constructor_expanddim(self):
        return DF


class DF(pd.DataFrame):
    def __repr__(self):
        foos = {k: getattr(v, "foo", None) for k, v in self.items()}
        return super().__repr__() + f"\n{foos=}"

    @property
    def _constructor(self):
        return DF

    @property
    def _constructor_sliced(self):
        return S


df = DF({"a": [1]})
df["a"].foo = "bar"
df.copy()  # ``DataFrame.copy`` mutates the data!
assert hasattr(df["a"], "foo"), "Dataframe mutated by ``copy`` method"
