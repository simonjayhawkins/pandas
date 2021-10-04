"""
This file contains a minimal set of tests for compliance with the extension
array interface test suite, and should contain no other tests.
The test suite for the full functionality of the array is located in
`pandas/tests/arrays/`.

The tests in this file are inherited from the BaseExtensionTests, and only
minimal tweaks should be applied to get the tests passing (by overwriting a
parent method).

Additional tests should either be added to one of the BaseExtensionTests
classes (if they are relevant for the extension interface for all dtypes), or
be added to the array-specific tests in `pandas/tests/arrays/`.

"""
import numpy as np
import pytest

import pandas.util._test_decorators as td

from pandas.core.dtypes.common import is_extension_array_dtype

import pandas as pd
import pandas._testing as tm
from pandas.api.types import is_float_dtype
from pandas.core.arrays.floating import (
    Float32Dtype,
    Float64Dtype,
)
from pandas.tests.extension import base


@pytest.fixture(
    params=[
        "numpy",
        pytest.param("cupy", marks=td.skip_if_no("cupy")),
    ]
)
def storage(request):
    """
    Parametrized fixture for floating array memory model.

    * 'numpy'
    * 'cupy'
    """
    return request.param


def make_data():
    return (
        list(np.arange(0.1, 0.9, 0.1))
        + [pd.NA]
        + list(np.arange(1, 9.8, 0.1))
        + [pd.NA]
        + [9.9, 10.0]
    )


@pytest.fixture(params=[Float32Dtype, Float64Dtype])
def dtype(request):
    return request.param()


@pytest.fixture
def data(dtype):
    return pd.array(make_data(), dtype=dtype)


@pytest.fixture
def data_for_twos(dtype):
    return pd.array(np.ones(100) * 2, dtype=dtype)


@pytest.fixture
def data_missing(dtype):
    return pd.array([pd.NA, 0.1], dtype=dtype)


@pytest.fixture
def data_for_sorting(dtype):
    return pd.array([0.1, 0.2, 0.0], dtype=dtype)


@pytest.fixture
def data_missing_for_sorting(dtype):
    return pd.array([0.1, pd.NA, 0.0], dtype=dtype)


@pytest.fixture
def na_cmp():
    # we are pd.NA
    return lambda x, y: x is pd.NA and y is pd.NA


@pytest.fixture
def na_value():
    return pd.NA


@pytest.fixture
def data_for_grouping(dtype):
    b = 0.1
    a = 0.0
    c = 0.2
    na = pd.NA
    return pd.array([b, b, na, na, a, a, b, c], dtype=dtype)


class TestDtype(base.BaseDtypeTests):
    @pytest.mark.skip(reason="using multiple dtypes")
    def test_is_dtype_unboxes_dtype(self):
        # we have multiple dtypes, so skip
        pass


class TestArithmeticOps(base.BaseArithmeticOpsTests):
    def check_opname(self, s, op_name, other, exc=None):
        # overwriting to indicate ops don't raise an error
        super().check_opname(s, op_name, other, exc=None)

    def _check_op(self, s, op, other, op_name, exc=NotImplementedError):
        if exc is None:
            sdtype = tm.get_dtype(s)
            if (
                hasattr(other, "dtype")
                and not is_extension_array_dtype(other.dtype)
                and is_float_dtype(other.dtype)
            ):
                # other is np.float64 and would therefore always result in
                # upcasting, so keeping other as same numpy_dtype
                other = other.astype(sdtype.numpy_dtype)

            result = op(s, other)
            expected = self._combine(s, other, op)

            # combine method result in 'biggest' (float64) dtype
            expected = expected.astype(sdtype)

            self.assert_equal(result, expected)
        else:
            with pytest.raises(exc):
                op(s, other)

    def _check_divmod_op(self, s, op, other, exc=None):
        super()._check_divmod_op(s, op, other, None)


class TestComparisonOps(base.BaseComparisonOpsTests):
    def _check_op(self, s, op, other, op_name, exc=NotImplementedError):
        if exc is None:
            result = op(s, other)
            # Override to do the astype to boolean
            expected = s.combine(other, op).astype("boolean")
            self.assert_series_equal(result, expected)
        else:
            with pytest.raises(exc):
                op(s, other)

    def check_opname(self, s, op_name, other, exc=None):
        super().check_opname(s, op_name, other, exc=None)

    def _compare_other(self, s, data, op_name, other):
        self.check_opname(s, op_name, other)


class TestInterface(base.BaseInterfaceTests):
    pass


class TestConstructors(base.BaseConstructorsTests):
    pass


class TestReshaping(base.BaseReshapingTests):
    pass


class TestGetitem(base.BaseGetitemTests):
    pass


class TestSetitem(base.BaseSetitemTests):
    pass


class TestMissing(base.BaseMissingTests):
    pass


class TestMethods(base.BaseMethodsTests):
    @pytest.mark.skip(reason="uses nullable integer")
    def test_value_counts(self, all_data, dropna):
        all_data = all_data[:10]
        if dropna:
            other = np.array(all_data[~all_data.isna()])
        else:
            other = all_data

        result = pd.Series(all_data).value_counts(dropna=dropna).sort_index()
        expected = pd.Series(other).value_counts(dropna=dropna).sort_index()
        expected.index = expected.index.astype(all_data.dtype)

        self.assert_series_equal(result, expected)

    @pytest.mark.skip(reason="uses nullable integer")
    def test_value_counts_with_normalize(self, data):
        pass


class TestCasting(base.BaseCastingTests):
    pass


class TestGroupby(base.BaseGroupbyTests):
    pass


class TestNumericReduce(base.BaseNumericReduceTests):
    def check_reduce(self, s, op_name, skipna):
        # overwrite to ensure pd.NA is tested instead of np.nan
        # https://github.com/pandas-dev/pandas/issues/30958
        result = getattr(s, op_name)(skipna=skipna)
        if not skipna and s.isna().any():
            expected = pd.NA
        else:
            expected = getattr(s.dropna().astype(s.dtype.numpy_dtype), op_name)(
                skipna=skipna
            )
        tm.assert_almost_equal(result, expected)


@pytest.mark.skip(reason="Tested in tests/reductions/test_reductions.py")
class TestBooleanReduce(base.BaseBooleanReduceTests):
    pass


class TestPrinting(base.BasePrintingTests):
    pass


class TestParsing(base.BaseParsingTests):
    pass
