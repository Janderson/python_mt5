# python_mt5
Python helper to extract data from Metatrader 5 - using new MT5 API.

## Some useful commands

To export data to csv 
python main.py export_bars --ticker EURUSD --timeframe H1
python main.py export_bars --ticker PETR4 --timeframe H1

Multiple tickers are also allowed
python main.py export_bars --ticker PETR4 --ticker VALE3 --timeframe H1 

It's possible to specify qtd bars will be downloaded
python main.py export_bars --ticker PETR4 --ticker VALE3 --timeframe H1 --bars 10000
