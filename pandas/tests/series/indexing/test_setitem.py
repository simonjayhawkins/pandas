from datetime import date

import numpy as np
import pytest

from pandas import MultiIndex, NaT, Series, Timestamp, date_range, period_range
from pandas.core.indexing import IndexingError
import pandas.testing as tm

from pandas.tseries.offsets import BDay


class TestSetitemDT64Values:
    def test_setitem_none_nan(self):
        series = Series(date_range("1/1/2000", periods=10))
        series[3] = None
        assert series[3] is NaT

        series[3:5] = None
        assert series[4] is NaT

        series[5] = np.nan
        assert series[5] is NaT

        series[5:7] = np.nan
        assert series[6] is NaT

    def test_setitem_multiindex_empty_slice(self):
        # https://github.com/pandas-dev/pandas/issues/35878
        idx = MultiIndex.from_tuples([("a", 1), ("b", 2)])
        result = Series([1, 2], index=idx)
        expected = result.copy()
        result.loc[[]] = 0
        tm.assert_series_equal(result, expected)

    def test_setitem_with_string_index(self):
        # GH#23451
        ser = Series([1, 2, 3], index=["Date", "b", "other"])
        ser["Date"] = date.today()
        assert ser.Date == date.today()
        assert ser["Date"] == date.today()

    def test_setitem_with_different_tz_casts_to_object(self):
        # GH#24024
        ser = Series(date_range("2000", periods=2, tz="US/Central"))
        ser[0] = Timestamp("2000", tz="US/Eastern")
        expected = Series(
            [
                Timestamp("2000-01-01 00:00:00-05:00", tz="US/Eastern"),
                Timestamp("2000-01-02 00:00:00-06:00", tz="US/Central"),
            ],
            dtype=object,
        )
        tm.assert_series_equal(ser, expected)


class TestSetitemPeriodDtype:
    @pytest.mark.parametrize("na_val", [None, np.nan])
    def test_setitem_na_period_dtype_casts_to_nat(self, na_val):
        ser = Series(period_range("2000-01-01", periods=10, freq="D"))

        ser[3] = na_val
        assert ser[3] is NaT

        ser[3:5] = na_val
        assert ser[4] is NaT


class TestSetitemBooleanMask:
    def test_setitem_boolean(self, string_series):
        mask = string_series > string_series.median()

        # similar indexed series
        result = string_series.copy()
        result[mask] = string_series * 2
        expected = string_series * 2
        tm.assert_series_equal(result[mask], expected[mask])

        # needs alignment
        result = string_series.copy()
        result[mask] = (string_series * 2)[0:5]
        expected = (string_series * 2)[0:5].reindex_like(string_series)
        expected[-mask] = string_series[mask]
        tm.assert_series_equal(result[mask], expected[mask])

    def test_setitem_boolean_corner(self, datetime_series):
        ts = datetime_series
        mask_shifted = ts.shift(1, freq=BDay()) > ts.median()

        msg = (
            r"Unalignable boolean Series provided as indexer \(index of "
            r"the boolean Series and of the indexed object do not match"
        )
        with pytest.raises(IndexingError, match=msg):
            ts[mask_shifted] = 1

        with pytest.raises(IndexingError, match=msg):
            ts.loc[mask_shifted] = 1

    def test_setitem_boolean_different_order(self, string_series):
        ordered = string_series.sort_values()

        copy = string_series.copy()
        copy[ordered > 0] = 0

        expected = string_series.copy()
        expected[expected > 0] = 0

        tm.assert_series_equal(copy, expected)


class TestSetitemViewCopySemantics:
    def test_setitem_invalidates_datetime_index_freq(self):
        # GH#24096 altering a datetime64tz Series inplace invalidates the
        #  `freq` attribute on the underlying DatetimeIndex

        dti = date_range("20130101", periods=3, tz="US/Eastern")
        ts = dti[1]
        ser = Series(dti)
        assert ser._values is not dti
        assert ser._values._data.base is not dti._data._data.base
        assert dti.freq == "D"
        ser.iloc[1] = NaT
        assert ser._values.freq is None

        # check that the DatetimeIndex was not altered in place
        assert ser._values is not dti
        assert ser._values._data.base is not dti._data._data.base
        assert dti[1] == ts
        assert dti.freq == "D"

    def test_dt64tz_setitem_does_not_mutate_dti(self):
        # GH#21907, GH#24096
        dti = date_range("2016-01-01", periods=10, tz="US/Pacific")
        ts = dti[0]
        ser = Series(dti)
        assert ser._values is not dti
        assert ser._values._data.base is not dti._data._data.base
        assert ser._mgr.blocks[0].values is not dti
        assert ser._mgr.blocks[0].values._data.base is not dti._data._data.base

        ser[::3] = NaT
        assert ser[0] is NaT
        assert dti[0] == ts


class TestSetitemCallable:
    def test_setitem_callable_key(self):
        # GH#12533
        ser = Series([1, 2, 3, 4], index=list("ABCD"))
        ser[lambda x: "A"] = -1

        expected = Series([-1, 2, 3, 4], index=list("ABCD"))
        tm.assert_series_equal(ser, expected)

    def test_setitem_callable_other(self):
        # GH#13299
        inc = lambda x: x + 1

        ser = Series([1, 2, -1, 4])
        ser[ser < 0] = inc

        expected = Series([1, 2, inc, 4])
        tm.assert_series_equal(ser, expected)
