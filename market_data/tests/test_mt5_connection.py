import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import MetaTrader5 as MT5
from market_data.mt5.mt5_connection import MT5Connection


def test_mt5_connection_start():
    mt5 = MT5Connection()
    mt5.open() 
    assert type(mt5.version) == str


def test_mt5_connection_timeframe_str_to_tf():
    mt5 = MT5Connection()
    mt5.open() 
    #import ipdb; ipdb.set_trace()
    assert mt5.str_timeframe_to_mt5("D1") == MT5.TIMEFRAME_D1
    assert mt5.str_timeframe_to_mt5("H1") == MT5.TIMEFRAME_H1
