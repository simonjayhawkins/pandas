"""
masked_reductions.py is for reduction algorithms using a mask-based approach
for missing values.
"""

import numpy as np

from pandas._libs import missing as libmissing
from pandas.compat.numpy import _np_version_under1p17

from pandas.core.nanops import check_below_min_count


def sum(
    values: np.ndarray, mask: np.ndarray, skipna: bool = True, min_count: int = 0,
):
    """
    Sum for 1D masked array.

    Parameters
    ----------
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation).
    mask : np.ndarray
        Boolean numpy array (True values indicate missing values).
    skipna : bool, default True
        Whether to skip NA.
    min_count : int, default 0
        The required number of valid values to perform the operation. If fewer than
        ``min_count`` non-NA values are present the result will be NA.
    """
    if not skipna:
        if mask.any():
            return libmissing.NA
        else:
            if check_below_min_count(values.shape, None, min_count):
                return libmissing.NA
            return np.sum(values)
    else:
        if check_below_min_count(values.shape, mask, min_count):
            return libmissing.NA

        if _np_version_under1p17:
            return np.sum(values[~mask])
        else:
            return np.sum(values, where=~mask)
