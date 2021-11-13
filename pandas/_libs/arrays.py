"""
Implementations for internal ExtensionArrays.
"""
from __future__ import annotations

from typing import (
    Literal,
    Sequence,
    TypeVar,
)

import numpy as np

from pandas._typing import (
    DtypeObj,
    Shape,
)

from pandas.core.arrays.base import ExtensionArray

_NDArrayBackedT = TypeVar("_NDArrayBackedT", bound="NDArrayBacked")


class NDArrayBacked(ExtensionArray):

    _dtype: DtypeObj
    _ndarray: np.ndarray

    def __init__(self, values: np.ndarray, dtype: DtypeObj):
        self._ndarray = values
        self._dtype = dtype

    @classmethod
    def _simple_new(
        cls: type[_NDArrayBackedT], values: np.ndarray, dtype: DtypeObj
    ) -> _NDArrayBackedT:
        obj = NDArrayBacked.__new__(cls)
        obj._ndarray = values
        obj._dtype = dtype
        return obj

    def _from_backing_data(
        self: _NDArrayBackedT, values: np.ndarray
    ) -> _NDArrayBackedT:
        """
        Construct a new ExtensionArray `new_array` with `arr` as its _ndarray.

        This should round-trip:
            self == self._from_backing_data(self._ndarray)
        """
        obj = NDArrayBacked.__new__(type(self))
        obj._ndarray = values
        obj._dtype = self._dtype
        return obj

    def __setstate__(self, state):
        if isinstance(state, dict):
            if "_data" in state:
                data = state.pop("_data")
            elif "_ndarray" in state:
                data = state.pop("_ndarray")
            else:
                raise ValueError
            self._ndarray = data
            self._dtype = state.pop("_dtype")

            for key, val in state.items():
                setattr(self, key, val)
        elif isinstance(state, tuple):
            if len(state) != 3:
                if len(state) == 1 and isinstance(state[0], dict):
                    self.__setstate__(state[0])
                    return
                raise NotImplementedError(state)

            data, dtype = state[:2]
            if isinstance(dtype, np.ndarray):
                dtype, data = data, dtype
            self._ndarray = data
            self._dtype = dtype

            if isinstance(state[2], dict):
                for key, val in state[2].items():
                    setattr(self, key, val)
            else:
                raise NotImplementedError(state)
        else:
            raise NotImplementedError(state)

    def __len__(self) -> int:
        return len(self._ndarray)

    @property
    def shape(self) -> Shape:
        return self._ndarray.shape

    @property
    def ndim(self) -> int:
        return self._ndarray.ndim

    @property
    def size(self) -> int:
        return self._ndarray.size

    @property
    def nbytes(self) -> int:
        return self._ndarray.nbytes

    def copy(self: _NDArrayBackedT) -> _NDArrayBackedT:
        res_values = self._ndarray.copy(order="A")
        return self._from_backing_data(res_values)

    def delete(self: _NDArrayBackedT, loc, axis=0) -> _NDArrayBackedT:
        res_values = np.delete(self._ndarray, loc, axis=axis)
        return self._from_backing_data(res_values)

    def swapaxes(self: _NDArrayBackedT, axis1: int, axis2: int) -> _NDArrayBackedT:
        res_values = self._ndarray.swapaxes(axis1, axis2)
        return self._from_backing_data(res_values)

    def repeat(
        self: _NDArrayBackedT, repeats: int | Sequence[int], axis: int | None = 0
    ) -> _NDArrayBackedT:
        if axis is None:
            axis = 0
        res_values = self._ndarray.repeat(repeats, axis)
        return self._from_backing_data(res_values)

    def reshape(self: _NDArrayBackedT, *args, **kwargs) -> _NDArrayBackedT:
        res_values = self._ndarray.reshape(*args, **kwargs)
        return self._from_backing_data(res_values)

    def ravel(
        self: _NDArrayBackedT, order: Literal["C", "F", "A", "K"] = "C"
    ) -> _NDArrayBackedT:
        res_values = self._ndarray.ravel(order)
        return self._from_backing_data(res_values)

    @property
    def T(self: _NDArrayBackedT) -> _NDArrayBackedT:
        res_values = self._ndarray.T
        return self._from_backing_data(res_values)
