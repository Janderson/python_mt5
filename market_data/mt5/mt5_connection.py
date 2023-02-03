from datetime import datetime
from datetime import timedelta
from MetaTrader5 import *
import MetaTrader5 as mt5
from pytz import timezone
import matplotlib.pyplot as plt
from . import mt5_converter
utc_tz = timezone('UTC')
 

class MT5Connection:
    def __init__(self):
        pass
    
    def open(self):
        # connect to MetaTrader 5
        return mt5.initialize()
        # wait till MetaTrader 5 establishes connection to the trade server and synchronizes the environment
        # mt5.MT5WaitForTerminal()

    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        mt5.shutdown()
        return True
    
    @property
    def version(self):
        return "{}.{}".format(mt5.version()[0], mt5.version()[1])

    def get_symbol_info(self, symbol_ticker):
        symbol_info = mt5.symbol_info(symbol_ticker)
        return {
            "ticker": symbol_ticker,
            "last": symbol_info.last,
            "ask": symbol_info.ask,
            "bid": symbol_info.bid,
            "open": symbol_info.session_open,
            "volume": symbol_info.session_volume,
            "time": symbol_info.time,
            "option_strike": symbol_info.option_strike,
            "option_underline": symbol_info.basis,
            "option_type": symbol_info.option_mode,
            "option_right": symbol_info.option_mode
        }

    def get_bars(self, symbol, timeframe, start_index=0, qtd=10):
        return mt5.copy_rates_from_pos(symbol, self.str_timeframe_to_mt5(timeframe), start_index, qtd)

    def get_ticks(self, symbol, start_date, qtd):
        ticks = mt5.copy_ticks_from(symbol, start_date, qtd, mt5.COPY_TICKS_ALL)
        return ticks

    def str_timeframe_to_mt5(self, tf_str):
        if tf_str == "D1":
            return mt5.TIMEFRAME_D1

        elif tf_str == "H1":
            return mt5.TIMEFRAME_H1

        elif tf_str == "M30":
            return mt5.TIMEFRAME_M30

        elif tf_str == "M15":
            return mt5.TIMEFRAME_M15

        elif tf_str == "M5":
            return mt5.TIMEFRAME_M5

        elif tf_str == "M1":
            return mt5.TIMEFRAME_M1
