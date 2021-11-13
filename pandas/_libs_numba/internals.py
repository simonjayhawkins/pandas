from typing import (
    TypeVar,
    final,
)

from pandas._libs.arrays import NDArrayBacked
from pandas._libs.internals import (
    BlockPlacement,
    SharedBlock,
)

_NDArrayBackedBlockT = TypeVar("_NDArrayBackedBlockT", bound="NDArrayBackedBlock")


class NDArrayBackedBlock(SharedBlock):
    """
    Block backed by NDArrayBackedExtensionArray
    """

    values: NDArrayBacked

    def __init__(self, values: NDArrayBacked, placement: BlockPlacement, ndim: int):
        # set values here the (implicit) call to SharedBlock.__cinit__ will
        #  set placement and ndim
        self.values = values

    @final
    def getitem_block_index(
        self: _NDArrayBackedBlockT, slicer: slice
    ) -> _NDArrayBackedBlockT:
        """
        Perform __getitem__-like specialized to slicing along index.

        Assumes self.ndim == 2
        """
        # error: No overload variant of "__getitem__" of "ExtensionArray"
        # matches argument type "Tuple[ellipsis, slice]"
        new_values = self.values[..., slicer]  # type:ignore[call-overload]
        return type(self)(new_values, self._mgr_locs, ndim=self.ndim)
