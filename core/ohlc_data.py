
import pandas as pd
import datetime
import dateutil.parser
from datetime import datetime, timedelta
from services.logger import Logger


class OhlcData:
    def __init__(self, _ohlc_data=None):
        self.logger = Logger(self.__class__.__name__).get()
        self._auction_tickers = None
        self._ohlc_data = _ohlc_data if _ohlc_data is not None else []

    def calculate_ohlc(self, df_ohlc):
        ohlc = {
            'open'     : [df_ohlc.head(1).open.item()],
            'high'     : [df_ohlc.high.max()],
            'low'      : [df_ohlc.low.min()],
            'close'    : [df_ohlc.tail(1).close.item()],
            'volume'   : [df_ohlc.volume.sum()],
            'trades'   : [df_ohlc.trades.sum()],
            'ticker'   : [df_ohlc.head(1).ticker.item()],
            'exchange' : [df_ohlc.head(1).exchange.item()],
        }
        return pd.DataFrame.from_dict(ohlc)

    @property
    def auction_tickers(self):
        return self._auction_tickers

    def to_df(self):
        return pd.DataFrame([i[0] for i in self._ohlc_data])

    def filter_by_ticker(self, ticker):
        dataframe = self.to_df()
        return dataframe[dataframe.ticker == ticker]

    @property
    def ohlc_data(self):
        return self._ohlc_data

    @property
    def assets(self):
        if len(self._ohlc_data) > 0:
            return self.to_df()["ticker"]

    @property
    def last_time(self):
        if len(self._ohlc_data) > 0:
            return pd.to_datetime(self.to_df()["time"], format="%Y-%m-%dT%H:%M:%S").max()

    def add_ohlc(self, ohlc_dict):
        if isinstance(ohlc_dict, dict):
            return self._ohlc_data.append([ohlc_dict])
        return None

    @staticmethod
    def create_from_market_data(market_data_response):
        if issubclass(market_data_response.__class__, BaseResponse):
            return OhlcData(market_data_response.ohlc_data)
        return None

    def __repr__(self):
        return str(self.to_df())

    def __len__(self):
        return len(self._ohlc_data)
