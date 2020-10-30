import numpy as np

import pandas as pd
from pandas import DataFrame, Series, date_range, timedelta_range
import pandas._testing as tm


class TestTimeSeries:
    def test_contiguous_boolean_preserve_freq(self):
        rng = date_range("1/1/2000", "3/1/2000", freq="B")

        mask = np.zeros(len(rng), dtype=bool)
        mask[10:20] = True

        masked = rng[mask]
        expected = rng[10:20]
        assert expected.freq == rng.freq
        tm.assert_index_equal(masked, expected)

        mask[22] = True
        masked = rng[mask]
        assert masked.freq is None

    def test_promote_datetime_date(self):
        rng = date_range("1/1/2000", periods=20)
        ts = Series(np.random.randn(20), index=rng)

        ts_slice = ts[5:]
        ts2 = ts_slice.copy()
        ts2.index = [x.date() for x in ts2.index]

        result = ts + ts2
        result2 = ts2 + ts
        expected = ts + ts[5:]
        expected.index = expected.index._with_freq(None)
        tm.assert_series_equal(result, expected)
        tm.assert_series_equal(result2, expected)

        # test asfreq
        result = ts2.asfreq("4H", method="ffill")
        expected = ts[5:].asfreq("4H", method="ffill")
        tm.assert_series_equal(result, expected)

        result = rng.get_indexer(ts2.index)
        expected = rng.get_indexer(ts_slice.index)
        tm.assert_numpy_array_equal(result, expected)

    def test_series_map_box_timedelta(self):
        # GH 11349
        s = Series(timedelta_range("1 day 1 s", periods=5, freq="h"))

        def f(x):
            return x.total_seconds()

        s.map(f)
        s.apply(f)
        DataFrame(s).applymap(f)

    def test_view_tz(self):
        # GH#24024
        ser = Series(pd.date_range("2000", periods=4, tz="US/Central"))
        result = ser.view("i8")
        expected = Series(
            [
                946706400000000000,
                946792800000000000,
                946879200000000000,
                946965600000000000,
            ]
        )
        tm.assert_series_equal(result, expected)
