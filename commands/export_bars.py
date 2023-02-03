from .command import Command
from core.symbol_tf import SymbolTF
from itertools import product
import os


class ExportBars(Command):
    _timeframes = []
    _tickers = []
    _path = None
    _bars = None
    _connection = None

    def __init__(self, conection):
        self._connection = conection

    def parameters(self, tickers, timeframes, path="", bars=250):
        self._tickers = tickers
        self._timeframes = timeframes
        self._path = path
        self._bars = bars

    def run(self):
        for ticker, timeframe in product(self._tickers, self._timeframes):
            print(f"exportando {ticker}-{timeframe} ({self._bars} bars)".format(self._bars, ticker, timeframe))
            try:
                bars_df = self._connection.get_bars_to_df(
                    SymbolTF(ticker, timeframe), qtd=self._bars)
            except Exception as e:
                print("error e: {}".format(e))
                import traceback
                traceback.print_exc()
            os.makedirs("data", exist_ok=True)
            bars_df.to_csv("data/{}_{}.csv".format(ticker, timeframe))

    def result(self):
        return 0
