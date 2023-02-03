# python_mt5
Python helper to extract data from Metatrader 5 - using new MT5 API.

## Some useful commands

### To export data to csv file
python main.py export_bars --tickers PETR4 --timeframes H1,D1
python main.py export_bars --tickers EURUSD --timeframes H1  
CSV files will be stored into data folder  

### Multiple tickers are also allowed
python main.py export_bars --tickers PETR4,VALE3 --timeframes H1,D1

### It's possible to specify qtd bars will be downloaded
python main.py export_bars --tickers PETR4,VALE3 --timeframes H1 --bars 10000
