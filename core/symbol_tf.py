class SymbolTF:
    def __init__(self, ticker, timeframe):
        self._ticker = ticker
        self._timeframe = timeframe
    
    @property
    def symbol(self):    
        return self._ticker

    @property
    def ticker(self):    
        return self._ticker
    
    @property
    def timeframe(self):
        return self._timeframe
