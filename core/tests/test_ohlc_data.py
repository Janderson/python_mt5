import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.ohlc_data import OhlcData

def test_ohlc_data():
    ohlc_data = OhlcData()

    ohlc_data.add_ohlc({
        "ticker": "GFSA3",
        "open": 8.90, "high": 8.94, "low": 8.90, "close": 8.92,
        "volume": 10.0, "trades": 1,
        "time": "2019-02-20T17:50:00"
    })

    ohlc_data.add_ohlc({
        "ticker": "GFSA3",
        "open": 8.87, "high": 8.96, "low": 8.87, "close": 8.95,
        "volume": 10.0, "trades": 1,
        "time": "2019-02-20T17:51:00"
    })

    ohlc_data.add_ohlc({
        "ticker": "GFSA3",
        "open": 8.87, "high": 8.99, "low": 8.87, "close": 8.96,
        "volume": 50.0, "trades": 1,
        "time": "2019-02-20T17:54:00"
    })

    ohlc_data.add_ohlc({
        "ticker": "GFSA3",
        "open": 8.94, "high": 8.94, "low": 8.94, "close": 8.94,
        "volume": 50.0, "trades": 1,
        "time": "2019-02-20T18:11:00"
    })

    #import ipdb; ipdb.set_trace()
    assert len(ohlc_data) == 4
    assert ohlc_data.to_df().iloc[-1].close == 8.94
    assert ohlc_data.to_df().iloc[-1].time == "2019-02-20T18:11:00"

def test_last_time():
    ohlc_data = OhlcData([])

    ohlc_data.add_ohlc({
        "ticker": "GFSA3",
        "open": 8.90, "high": 8.94, "low": 8.90, "close": 8.92,
        "volume": 10.0, "trades": 1,
        "time": "2019-02-21T10:14:00"
    })

    ohlc_data.add_ohlc({
        "ticker": "GFSA3",
        "open": 8.87, "high": 8.96, "low": 8.87, "close": 8.95,
        "volume": 10.0, "trades": 1,
        "time": "2019-02-20T17:51:00"
    })

    assert len(ohlc_data) == 2

    assert str(ohlc_data.last_time) == "2019-02-21 10:14:00"

    ohlc_data.add_ohlc({
        "ticker": "GFSA3",
        "open": 8.87, "high": 8.96, "low": 8.87, "close": 8.95,
        "volume": 10.0, "trades": 1,
        "time": "2019-02-21T13:52:00"
    })
    assert str(ohlc_data.last_time) == "2019-02-21 13:52:00"

    ohlc_data.add_ohlc({
        "ticker": "GFSA3",
        "open": 8.87, "high": 8.96, "low": 8.87, "close": 8.95,
        "volume": 10.0, "trades": 1,
        "time": "2019-02-19T13:51:00"
    })
    assert str(ohlc_data.last_time) != "2019-02-19 13:51:00"