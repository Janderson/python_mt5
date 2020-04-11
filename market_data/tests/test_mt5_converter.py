import sys, os, pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from MetaTrader5 import *
import datetime
from market_data.mt5.mt5_connection import MT5Connection
from market_data.mt5.mt5_converter import MT5Converter
from core.symbol_tf import SymbolTF
from unittest.mock import Mock

@pytest.fixture
def tuple_to_inject():
    return (
        ((datetime.datetime(2019, 10, 21, 21, 0), 27.8, 28.68, 27.77, 28.57, 68244, 1, 63736500)), 
        ((datetime.datetime(2019, 10, 22, 21, 0), 28.53, 29.08, 28.45, 28.95, 40400, 1, 45781200)), 
        ((datetime.datetime(2019, 10, 23, 21, 0), 29.15, 29.25, 28.23, 28.32, 68413, 1, 60372900)), 
        ((datetime.datetime(2019, 10, 24, 21, 0), 29.2, 29.55, 29.01, 29.25, 109667, 1, 74141700)), 
        ((datetime.datetime(2019, 10, 27, 21, 0), 29.22, 29.66, 29.12, 29.58, 40836, 0, 36987000))
    )

def test_mt5_converter_start(tuple_to_inject):
    mt5 = MT5Connection()
    mt5.get_bars = Mock(return_value=tuple_to_inject)
    mt5_converter = MT5Converter(mt5)
    mt5_converter.get_bars_to_ohlc(SymbolTF("PETR4", "D1"))
    print(mt5.version)
