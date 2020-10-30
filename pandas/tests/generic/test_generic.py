from copy import copy, deepcopy

import numpy as np
import pytest

from pandas.core.dtypes.common import is_scalar

import pandas as pd
from pandas import DataFrame, Series, date_range
import pandas._testing as tm

# ----------------------------------------------------------------------
# Generic types test cases


class Generic:
    @property
    def _ndim(self):
        return self._typ._AXIS_LEN

    def _axes(self):
        """ return the axes for my object typ """
        return self._typ._AXIS_ORDERS

    def _construct(self, shape, value=None, dtype=None, **kwargs):
        """
        construct an object for the given shape
        if value is specified use that if its a scalar
        if value is an array, repeat it as needed
        """
        if isinstance(shape, int):
            shape = tuple([shape] * self._ndim)
        if value is not None:
            if is_scalar(value):
                if value == "empty":
                    arr = None
                    dtype = np.float64

                    # remove the info axis
                    kwargs.pop(self._typ._info_axis_name, None)
                else:
                    arr = np.empty(shape, dtype=dtype)
                    arr.fill(value)
            else:
                fshape = np.prod(shape)
                arr = value.ravel()
                new_shape = fshape / arr.shape[0]
                if fshape % arr.shape[0] != 0:
                    raise Exception("invalid value passed in _construct")

                arr = np.repeat(arr, new_shape).reshape(shape)
        else:
            arr = np.random.randn(*shape)
        return self._typ(arr, dtype=dtype, **kwargs)

    def _compare(self, result, expected):
        self._comparator(result, expected)

    def test_rename(self):

        # single axis
        idx = list("ABCD")
        # relabeling values passed into self.rename
        args = [
            str.lower,
            {x: x.lower() for x in idx},
            Series({x: x.lower() for x in idx}),
        ]

        for axis in self._axes():
            kwargs = {axis: idx}
            obj = self._construct(4, **kwargs)

            for arg in args:
                # rename a single axis
                result = obj.rename(**{axis: arg})
                expected = obj.copy()
                setattr(expected, axis, list("abcd"))
                self._compare(result, expected)

        # multiple axes at once

    def test_get_numeric_data(self):

        n = 4
        kwargs = {
            self._typ._get_axis_name(i): list(range(n)) for i in range(self._ndim)
        }

        # get the numeric data
        o = self._construct(n, **kwargs)
        result = o._get_numeric_data()
        self._compare(result, o)

        # non-inclusion
        result = o._get_bool_data()
        expected = self._construct(n, value="empty", **kwargs)
        self._compare(result, expected)

        # get the bool data
        arr = np.array([True, True, False, True])
        o = self._construct(n, value=arr, **kwargs)
        result = o._get_numeric_data()
        self._compare(result, o)

        # _get_numeric_data is includes _get_bool_data, so can't test for
        # non-inclusion

    def test_nonzero(self):

        # GH 4633
        # look at the boolean/nonzero behavior for objects
        obj = self._construct(shape=4)
        msg = f"The truth value of a {self._typ.__name__} is ambiguous"
        with pytest.raises(ValueError, match=msg):
            bool(obj == 0)
        with pytest.raises(ValueError, match=msg):
            bool(obj == 1)
        with pytest.raises(ValueError, match=msg):
            bool(obj)

        obj = self._construct(shape=4, value=1)
        with pytest.raises(ValueError, match=msg):
            bool(obj == 0)
        with pytest.raises(ValueError, match=msg):
            bool(obj == 1)
        with pytest.raises(ValueError, match=msg):
            bool(obj)

        obj = self._construct(shape=4, value=np.nan)
        with pytest.raises(ValueError, match=msg):
            bool(obj == 0)
        with pytest.raises(ValueError, match=msg):
            bool(obj == 1)
        with pytest.raises(ValueError, match=msg):
            bool(obj)

        # empty
        obj = self._construct(shape=0)
        with pytest.raises(ValueError, match=msg):
            bool(obj)

        # invalid behaviors

        obj1 = self._construct(shape=4, value=1)
        obj2 = self._construct(shape=4, value=1)

        with pytest.raises(ValueError, match=msg):
            if obj1:
                pass

        with pytest.raises(ValueError, match=msg):
            obj1 and obj2
        with pytest.raises(ValueError, match=msg):
            obj1 or obj2
        with pytest.raises(ValueError, match=msg):
            not obj1

    def test_downcast(self):
        # test close downcasting

        o = self._construct(shape=4, value=9, dtype=np.int64)
        result = o.copy()
        result._mgr = o._mgr.downcast()
        self._compare(result, o)

        o = self._construct(shape=4, value=9.5)
        result = o.copy()
        result._mgr = o._mgr.downcast()
        self._compare(result, o)

    def test_constructor_compound_dtypes(self):
        # see gh-5191
        # Compound dtypes should raise NotImplementedError.

        def f(dtype):
            return self._construct(shape=3, value=1, dtype=dtype)

        msg = (
            "compound dtypes are not implemented "
            f"in the {self._typ.__name__} constructor"
        )

        with pytest.raises(NotImplementedError, match=msg):
            f([("A", "datetime64[h]"), ("B", "str"), ("C", "int32")])

        # these work (though results may be unexpected)
        f("int64")
        f("float64")
        f("M8[ns]")

    def check_metadata(self, x, y=None):
        for m in x._metadata:
            v = getattr(x, m, None)
            if y is None:
                assert v is None
            else:
                assert v == getattr(y, m, None)

    def test_metadata_propagation(self):
        # check that the metadata matches up on the resulting ops

        o = self._construct(shape=3)
        o.name = "foo"
        o2 = self._construct(shape=3)
        o2.name = "bar"

        # ----------
        # preserving
        # ----------

        # simple ops with scalars
        for op in ["__add__", "__sub__", "__truediv__", "__mul__"]:
            result = getattr(o, op)(1)
            self.check_metadata(o, result)

        # ops with like
        for op in ["__add__", "__sub__", "__truediv__", "__mul__"]:
            result = getattr(o, op)(o)
            self.check_metadata(o, result)

        # simple boolean
        for op in ["__eq__", "__le__", "__ge__"]:
            v1 = getattr(o, op)(o)
            self.check_metadata(o, v1)
            self.check_metadata(o, v1 & v1)
            self.check_metadata(o, v1 | v1)

        # combine_first
        result = o.combine_first(o2)
        self.check_metadata(o, result)

        # ---------------------------
        # non-preserving (by default)
        # ---------------------------

        # add non-like
        result = o + o2
        self.check_metadata(result)

        # simple boolean
        for op in ["__eq__", "__le__", "__ge__"]:

            # this is a name matching op
            v1 = getattr(o, op)(o)
            v2 = getattr(o, op)(o2)
            self.check_metadata(v2)
            self.check_metadata(v1 & v2)
            self.check_metadata(v1 | v2)

    def test_head_tail(self, index):
        # GH5370

        o = self._construct(shape=len(index))

        axis = o._get_axis_name(0)
        setattr(o, axis, index)

        o.head()

        self._compare(o.head(), o.iloc[:5])
        self._compare(o.tail(), o.iloc[-5:])

        # 0-len
        self._compare(o.head(0), o.iloc[0:0])
        self._compare(o.tail(0), o.iloc[0:0])

        # bounded
        self._compare(o.head(len(o) + 1), o)
        self._compare(o.tail(len(o) + 1), o)

        # neg index
        self._compare(o.head(-3), o.head(len(index) - 3))
        self._compare(o.tail(-3), o.tail(len(index) - 3))

    def test_size_compat(self):
        # GH8846
        # size property should be defined

        o = self._construct(shape=10)
        assert o.size == np.prod(o.shape)
        assert o.size == 10 ** len(o.axes)

    def test_split_compat(self):
        # xref GH8846
        o = self._construct(shape=10)
        assert len(np.array_split(o, 5)) == 5
        assert len(np.array_split(o, 2)) == 2

    # See gh-12301
    def test_stat_unexpected_keyword(self):
        obj = self._construct(5)
        starwars = "Star Wars"
        errmsg = "unexpected keyword"

        with pytest.raises(TypeError, match=errmsg):
            obj.max(epic=starwars)  # stat_function
        with pytest.raises(TypeError, match=errmsg):
            obj.var(epic=starwars)  # stat_function_ddof
        with pytest.raises(TypeError, match=errmsg):
            obj.sum(epic=starwars)  # cum_function
        with pytest.raises(TypeError, match=errmsg):
            obj.any(epic=starwars)  # logical_function

    @pytest.mark.parametrize("func", ["sum", "cumsum", "any", "var"])
    def test_api_compat(self, func):

        # GH 12021
        # compat for __name__, __qualname__

        obj = self._construct(5)
        f = getattr(obj, func)
        assert f.__name__ == func
        assert f.__qualname__.endswith(func)

    def test_stat_non_defaults_args(self):
        obj = self._construct(5)
        out = np.array([0])
        errmsg = "the 'out' parameter is not supported"

        with pytest.raises(ValueError, match=errmsg):
            obj.max(out=out)  # stat_function
        with pytest.raises(ValueError, match=errmsg):
            obj.var(out=out)  # stat_function_ddof
        with pytest.raises(ValueError, match=errmsg):
            obj.sum(out=out)  # cum_function
        with pytest.raises(ValueError, match=errmsg):
            obj.any(out=out)  # logical_function

    def test_truncate_out_of_bounds(self):
        # GH11382

        # small
        shape = [int(2e3)] + ([1] * (self._ndim - 1))
        small = self._construct(shape, dtype="int8", value=1)
        self._compare(small.truncate(), small)
        self._compare(small.truncate(before=0, after=3e3), small)
        self._compare(small.truncate(before=-1, after=2e3), small)

        # big
        shape = [int(2e6)] + ([1] * (self._ndim - 1))
        big = self._construct(shape, dtype="int8", value=1)
        self._compare(big.truncate(), big)
        self._compare(big.truncate(before=0, after=3e6), big)
        self._compare(big.truncate(before=-1, after=2e6), big)

    @pytest.mark.parametrize(
        "func",
        [copy, deepcopy, lambda x: x.copy(deep=False), lambda x: x.copy(deep=True)],
    )
    @pytest.mark.parametrize("shape", [0, 1, 2])
    def test_copy_and_deepcopy(self, shape, func):
        # GH 15444
        obj = self._construct(shape)
        obj_copy = func(obj)
        assert obj_copy is not obj
        self._compare(obj_copy, obj)

    @pytest.mark.parametrize(
        "periods,fill_method,limit,exp",
        [
            (1, "ffill", None, [np.nan, np.nan, np.nan, 1, 1, 1.5, 0, 0]),
            (1, "ffill", 1, [np.nan, np.nan, np.nan, 1, 1, 1.5, 0, np.nan]),
            (1, "bfill", None, [np.nan, 0, 0, 1, 1, 1.5, np.nan, np.nan]),
            (1, "bfill", 1, [np.nan, np.nan, 0, 1, 1, 1.5, np.nan, np.nan]),
            (-1, "ffill", None, [np.nan, np.nan, -0.5, -0.5, -0.6, 0, 0, np.nan]),
            (-1, "ffill", 1, [np.nan, np.nan, -0.5, -0.5, -0.6, 0, np.nan, np.nan]),
            (-1, "bfill", None, [0, 0, -0.5, -0.5, -0.6, np.nan, np.nan, np.nan]),
            (-1, "bfill", 1, [np.nan, 0, -0.5, -0.5, -0.6, np.nan, np.nan, np.nan]),
        ],
    )
    def test_pct_change(self, periods, fill_method, limit, exp):
        vals = [np.nan, np.nan, 1, 2, 4, 10, np.nan, np.nan]
        obj = self._typ(vals)
        func = getattr(obj, "pct_change")
        res = func(periods=periods, fill_method=fill_method, limit=limit)
        if type(obj) is DataFrame:
            tm.assert_frame_equal(res, DataFrame(exp))
        else:
            tm.assert_series_equal(res, Series(exp))


class TestNDFrame:
    # tests that don't fit elsewhere

    def test_squeeze(self):
        # noop
        for s in [tm.makeFloatSeries(), tm.makeStringSeries(), tm.makeObjectSeries()]:
            tm.assert_series_equal(s.squeeze(), s)
        for df in [tm.makeTimeDataFrame()]:
            tm.assert_frame_equal(df.squeeze(), df)

        # squeezing
        df = tm.makeTimeDataFrame().reindex(columns=["A"])
        tm.assert_series_equal(df.squeeze(), df["A"])

        # don't fail with 0 length dimensions GH11229 & GH8999
        empty_series = Series([], name="five", dtype=np.float64)
        empty_frame = DataFrame([empty_series])
        tm.assert_series_equal(empty_series, empty_series.squeeze())
        tm.assert_series_equal(empty_series, empty_frame.squeeze())

        # axis argument
        df = tm.makeTimeDataFrame(nper=1).iloc[:, :1]
        assert df.shape == (1, 1)
        tm.assert_series_equal(df.squeeze(axis=0), df.iloc[0])
        tm.assert_series_equal(df.squeeze(axis="index"), df.iloc[0])
        tm.assert_series_equal(df.squeeze(axis=1), df.iloc[:, 0])
        tm.assert_series_equal(df.squeeze(axis="columns"), df.iloc[:, 0])
        assert df.squeeze() == df.iloc[0, 0]
        msg = "No axis named 2 for object type DataFrame"
        with pytest.raises(ValueError, match=msg):
            df.squeeze(axis=2)
        msg = "No axis named x for object type DataFrame"
        with pytest.raises(ValueError, match=msg):
            df.squeeze(axis="x")

        df = tm.makeTimeDataFrame(3)
        tm.assert_frame_equal(df.squeeze(axis=0), df)

    def test_numpy_squeeze(self):
        s = tm.makeFloatSeries()
        tm.assert_series_equal(np.squeeze(s), s)

        df = tm.makeTimeDataFrame().reindex(columns=["A"])
        tm.assert_series_equal(np.squeeze(df), df["A"])

    def test_transpose(self):
        for s in [tm.makeFloatSeries(), tm.makeStringSeries(), tm.makeObjectSeries()]:
            # calls implementation in pandas/core/base.py
            tm.assert_series_equal(s.transpose(), s)
        for df in [tm.makeTimeDataFrame()]:
            tm.assert_frame_equal(df.transpose().transpose(), df)

    def test_numpy_transpose(self):
        msg = "the 'axes' parameter is not supported"

        s = tm.makeFloatSeries()
        tm.assert_series_equal(np.transpose(s), s)

        with pytest.raises(ValueError, match=msg):
            np.transpose(s, axes=1)

        df = tm.makeTimeDataFrame()
        tm.assert_frame_equal(np.transpose(np.transpose(df)), df)

        with pytest.raises(ValueError, match=msg):
            np.transpose(df, axes=1)

    def test_take(self):
        indices = [1, 5, -2, 6, 3, -1]
        for s in [tm.makeFloatSeries(), tm.makeStringSeries(), tm.makeObjectSeries()]:
            out = s.take(indices)
            expected = Series(
                data=s.values.take(indices), index=s.index.take(indices), dtype=s.dtype
            )
            tm.assert_series_equal(out, expected)
        for df in [tm.makeTimeDataFrame()]:
            out = df.take(indices)
            expected = DataFrame(
                data=df.values.take(indices, axis=0),
                index=df.index.take(indices),
                columns=df.columns,
            )
            tm.assert_frame_equal(out, expected)

    def test_take_invalid_kwargs(self):
        indices = [-3, 2, 0, 1]
        s = tm.makeFloatSeries()
        df = tm.makeTimeDataFrame()

        for obj in (s, df):
            msg = r"take\(\) got an unexpected keyword argument 'foo'"
            with pytest.raises(TypeError, match=msg):
                obj.take(indices, foo=2)

            msg = "the 'out' parameter is not supported"
            with pytest.raises(ValueError, match=msg):
                obj.take(indices, out=indices)

            msg = "the 'mode' parameter is not supported"
            with pytest.raises(ValueError, match=msg):
                obj.take(indices, mode="clip")

    @pytest.mark.parametrize("is_copy", [True, False])
    def test_depr_take_kwarg_is_copy(self, is_copy):
        # GH 27357
        df = DataFrame({"A": [1, 2, 3]})
        msg = (
            "is_copy is deprecated and will be removed in a future version. "
            "'take' always returns a copy, so there is no need to specify this."
        )
        with tm.assert_produces_warning(FutureWarning) as w:
            df.take([0, 1], is_copy=is_copy)

        assert w[0].message.args[0] == msg

        s = Series([1, 2, 3])
        with tm.assert_produces_warning(FutureWarning):
            s.take([0, 1], is_copy=is_copy)

    def test_equals(self):
        # Add object dtype column with nans
        index = np.random.random(10)
        df1 = DataFrame(np.random.random(10), index=index, columns=["floats"])
        df1["text"] = "the sky is so blue. we could use more chocolate.".split()
        df1["start"] = date_range("2000-1-1", periods=10, freq="T")
        df1["end"] = date_range("2000-1-1", periods=10, freq="D")
        df1["diff"] = df1["end"] - df1["start"]
        df1["bool"] = np.arange(10) % 3 == 0
        df1.loc[::2] = np.nan
        df2 = df1.copy()
        assert df1["text"].equals(df2["text"])
        assert df1["start"].equals(df2["start"])
        assert df1["end"].equals(df2["end"])
        assert df1["diff"].equals(df2["diff"])
        assert df1["bool"].equals(df2["bool"])
        assert df1.equals(df2)
        assert not df1.equals(object)

        # different dtype
        different = df1.copy()
        different["floats"] = different["floats"].astype("float32")
        assert not df1.equals(different)

        # different index
        different_index = -index
        different = df2.set_index(different_index)
        assert not df1.equals(different)

        # different columns
        different = df2.copy()
        different.columns = df2.columns[::-1]
        assert not df1.equals(different)

        # DatetimeIndex
        index = pd.date_range("2000-1-1", periods=10, freq="T")
        df1 = df1.set_index(index)
        df2 = df1.copy()
        assert df1.equals(df2)

        # MultiIndex
        df3 = df1.set_index(["text"], append=True)
        df2 = df1.set_index(["text"], append=True)
        assert df3.equals(df2)

        df2 = df1.set_index(["floats"], append=True)
        assert not df3.equals(df2)

        # NaN in index
        df3 = df1.set_index(["floats"], append=True)
        df2 = df1.set_index(["floats"], append=True)
        assert df3.equals(df2)

    @pytest.mark.parametrize("box", [pd.Series, pd.DataFrame])
    def test_axis_classmethods(self, box):
        obj = box(dtype=object)
        values = box._AXIS_TO_AXIS_NUMBER.keys()
        for v in values:
            assert obj._get_axis_number(v) == box._get_axis_number(v)
            assert obj._get_axis_name(v) == box._get_axis_name(v)
            assert obj._get_block_manager_axis(v) == box._get_block_manager_axis(v)

    @pytest.mark.parametrize("box", [pd.Series, pd.DataFrame])
    def test_axis_names_deprecated(self, box):
        # GH33637
        obj = box(dtype=object)
        with tm.assert_produces_warning(FutureWarning, check_stacklevel=False):
            obj._AXIS_NAMES

    @pytest.mark.parametrize("box", [pd.Series, pd.DataFrame])
    def test_axis_numbers_deprecated(self, box):
        # GH33637
        obj = box(dtype=object)
        with tm.assert_produces_warning(FutureWarning, check_stacklevel=False):
            obj._AXIS_NUMBERS

    @pytest.mark.parametrize("as_frame", [True, False])
    def test_flags_identity(self, as_frame):
        s = Series([1, 2])
        if as_frame:
            s = s.to_frame()

        assert s.flags is s.flags
        s2 = s.copy()
        assert s2.flags is not s.flags
