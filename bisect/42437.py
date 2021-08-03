# BUG: Assigning extension array value to series of dtype object fails if element type is array-like #42437

import pandas as pd
from pandas.api.extensions import (
    ExtensionArray,
    ExtensionDtype,
)

print(pd.__version__)


class StubDtype(ExtensionDtype):
    """Extension dtype whose elements are something that numpy.asarray()
    will turn into an array (in this case a tuple)"""

    def __init__(self):
        pass

    @property
    def type(self):
        return tuple

    @property
    def name(self) -> str:
        return "StubDtype"

    @classmethod
    def construct_array_type(cls):
        return StubExtensionArray()


class StubExtensionArray(ExtensionArray):
    """Just enough of an extension array to run the four lines of code
    that follow."""

    @property
    def dtype(self):
        return StubDtype()

    def copy(self):
        return StubExtensionArray()

    def __len__(self):
        return 5

    def __getitem__(self, key):
        # Every position in the array has the tuple (1, 2, 3)
        return (1, 2, 3)


data = StubExtensionArray()
series1 = pd.Series(data, name="data")
series2 = pd.Series(index=series1.index, dtype=object, name="data")
series2.loc[series1.index] = data
