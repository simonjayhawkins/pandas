# BUG: extraneous copy of extension arrays in v1.3.0 #42501

import pandas as pd
from pandas.core.arrays.integer import coerce_to_array

print(pd.__version__)

import pandas as pd


class IntegerArrayNoCopy(pd.core.arrays.IntegerArray):
    @classmethod
    def _from_sequence(cls, scalars, *, dtype=None, copy=False):
        values, mask = coerce_to_array(scalars, dtype=dtype, copy=copy)
        return IntegerArrayNoCopy(values, mask)

    def copy(self):
        raise NotImplementedError


class Int16DtypeNoCopy(pd.Int16Dtype):
    @classmethod
    def construct_array_type(cls):
        return IntegerArrayNoCopy


df = pd.DataFrame({"col": [1, 4, None, 5]}, dtype=object)
result = df.astype({"col": Int16DtypeNoCopy()}, copy=False)
print(result)
