"""
Series.__getitem__ test classes are organized by the type of key passed.
"""
from datetime import datetime

import numpy as np
import pytest

from pandas._libs.tslibs import conversion, timezones

import pandas as pd
from pandas import Series, Timestamp, date_range, period_range
import pandas._testing as tm


class TestSeriesGetitemScalars:

    # TODO: better name/GH ref?
    def test_getitem_regression(self):
        ser = Series(range(5), index=list(range(5)))
        result = ser[list(range(5))]
        tm.assert_series_equal(result, ser)

    # ------------------------------------------------------------------
    # Series with DatetimeIndex

    @pytest.mark.parametrize("tzstr", ["Europe/Berlin", "dateutil/Europe/Berlin"])
    def test_getitem_pydatetime_tz(self, tzstr):
        tz = timezones.maybe_get_tz(tzstr)

        index = date_range(
            start="2012-12-24 16:00", end="2012-12-24 18:00", freq="H", tz=tzstr
        )
        ts = Series(index=index, data=index.hour)
        time_pandas = Timestamp("2012-12-24 17:00", tz=tzstr)

        dt = datetime(2012, 12, 24, 17, 0)
        time_datetime = conversion.localize_pydatetime(dt, tz)
        assert ts[time_pandas] == ts[time_datetime]

    @pytest.mark.parametrize("tz", ["US/Eastern", "dateutil/US/Eastern"])
    def test_string_index_alias_tz_aware(self, tz):
        rng = date_range("1/1/2000", periods=10, tz=tz)
        ser = Series(np.random.randn(len(rng)), index=rng)

        result = ser["1/3/2000"]
        tm.assert_almost_equal(result, ser[2])


class TestSeriesGetitemSlices:
    def test_getitem_slice_2d(self, datetime_series):
        # GH#30588 multi-dimensional indexing deprecated

        # This is currently failing because the test was relying on
        # the DeprecationWarning coming through Index.__getitem__.
        # We want to implement a warning specifically for Series.__getitem__
        # at which point this will become a Deprecation/FutureWarning
        with tm.assert_produces_warning(None):
            # GH#30867 Don't want to support this long-term, but
            # for now ensure that the warning from Index
            # doesn't comes through via Series.__getitem__.
            result = datetime_series[:, np.newaxis]
        expected = datetime_series.values[:, np.newaxis]
        tm.assert_almost_equal(result, expected)

    # FutureWarning from NumPy.
    @pytest.mark.filterwarnings("ignore:Using a non-tuple:FutureWarning")
    def test_getitem_median_slice_bug(self):
        index = date_range("20090415", "20090519", freq="2B")
        s = Series(np.random.randn(13), index=index)

        indexer = [slice(6, 7, None)]
        with tm.assert_produces_warning(FutureWarning):
            # GH#31299
            result = s[indexer]
        expected = s[indexer[0]]
        tm.assert_series_equal(result, expected)


class TestSeriesGetitemListLike:
    def test_getitem_intlist_intindex_periodvalues(self):
        ser = Series(period_range("2000-01-01", periods=10, freq="D"))

        result = ser[[2, 4]]
        exp = pd.Series(
            [pd.Period("2000-01-03", freq="D"), pd.Period("2000-01-05", freq="D")],
            index=[2, 4],
            dtype="Period[D]",
        )
        tm.assert_series_equal(result, exp)
        assert result.dtype == "Period[D]"


def test_getitem_generator(string_series):
    gen = (x > 0 for x in string_series)
    result = string_series[gen]
    result2 = string_series[iter(string_series > 0)]
    expected = string_series[string_series > 0]
    tm.assert_series_equal(result, expected)
    tm.assert_series_equal(result2, expected)
