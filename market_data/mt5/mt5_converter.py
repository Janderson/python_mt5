from core.symbol_tf import SymbolTF
from core.ohlc_data import OhlcData
import pandas as pd
from datetime import datetime

class MT5Converter:
    def __init__(self, mt5_connection):
        self._mt5_connection = mt5_connection
    
    def get_bars_to_df(self, symbol_tf, start_index=0, qtd=1):
        if not isinstance(symbol_tf, SymbolTF):
            return False
        
        rates = self._mt5_connection.get_bars(symbol_tf.symbol, symbol_tf.timeframe, start_index=start_index, qtd=qtd)
        #import ipdb; ipdb.set_trace()
        rates_dataframe = pd.DataFrame(rates,
                           columns=['time', 'open', 'low', 'high', 'close', 'tick_volume', 'spread', 'real_volume'])

                # get a UTC time offset for the local PC
        UTC_OFFSET_TIMEDELTA = datetime.utcnow() - datetime.now()
        
        # create a simple function correcting the offset head-on
        def local_to_utc(dt):
            return dt + UTC_OFFSET_TIMEDELTA
        

        #rates_dataframe['time'] = rates_dataframe.apply(lambda rate: local_to_utc(rate['time']), axis=1)
        rates_dataframe['time'] = pd.to_datetime(rates_dataframe['time'], unit="s")
        rates_dataframe['ticker'] = symbol_tf.ticker
        rates_dataframe['timeframe'] = symbol_tf.timeframe
        # apply the offset for the 'time' column in the rates_frame dataframe
        return rates_dataframe

    def get_bars_to_ohlc(self, symbol_tf, start_index=0, qtd=1):
        if not isinstance(symbol_tf, SymbolTF):
            return False
        
        rates = self._mt5_connection.get_bars(symbol_tf.symbol, symbol_tf.timeframe, start_index=start_index, qtd=qtd)
        ohlc = OhlcData()
        rates_frame = pd.DataFrame(list(rates),
                           columns=['time', 'open', 'low', 'high', 'close', 'tick_volume', 'spread', 'real_volume'])

                # get a UTC time offset for the local PC
        UTC_OFFSET_TIMEDELTA = datetime.utcnow() - datetime.now()
        
        # create a simple function correcting the offset head-on
        def local_to_utc(dt):
            return dt + UTC_OFFSET_TIMEDELTA
        
        # apply the offset for the 'time' column in the rates_frame dataframe
        rates_frame['time'] = rates_frame.apply(lambda rate: local_to_utc(rate['time']), axis=1)
        print(rates_frame)
        for mt5_rate in rates:
            print(mt5_rate)
        