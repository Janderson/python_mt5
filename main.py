from core.symbol_tf import SymbolTF
from commands.export_bars import ExportBars
from market_data.mt5.mt5_converter import MT5Converter
from market_data.mt5.mt5_connection import MT5Connection
from time import sleep
from datetime import datetime, timedelta, date
import click
import os
import pandas as pd

@click.group(chain=True)
def cli():
    pass

def export_data_to_csv():
    stocks = ["WIN$N", "BOVA11"]

    with MT5Connection() as mt5_connection:
        mt5 = MT5Converter(mt5_connection)
        for stock in stocks:
            time_frame = "D1"
            bars_df = mt5.get_bars_to_df(SymbolTF(stock, time_frame), qtd=500000)
            bars_df.to_csv("data/{}_{}.csv".format(stock, time_frame))
            print("{} - {}".format(stock,time_frame))

@cli.command('export_bars')
@click.option('--bars', default=500, help='Number of Bars to download.')
@click.option('--qtd_loop', default=1, help='The person to greet.')
@click.option('timeframes', '--timeframe', default=["D1"], multiple=True, help='TimeFrame to export.')
@click.option('tickers', '--ticker', default=["PETR4"], multiple=True, help='Stocks to export.')
def export_bars(bars, qtd_loop, timeframes, tickers):
    with MT5Connection() as mt5_connection:
        exportbars_cmd = ExportBars(MT5Converter(mt5_connection))
        exportbars_cmd.parameters(tickers = list(tickers), 
                                  timeframes = list(timeframes), bars=bars)
        print(exportbars_cmd._tickers, exportbars_cmd._timeframes)
        exportbars_cmd.run()

@cli.command('monitor_ticks')
def monitor_ticks():
    stocks = ["WINJ20", "BOVA11", "FESA4", "OIBR3", "PETR4", "PETRX250", "IBOV", "BOVV11", "XBOV11", "INDJ20", "PETRE152", "PETRE172", "PETRE202"]
    prices={}
    for i in range(105000):
            with MT5Connection() as mt5_connection:
                #import ipdb; ipdb.set_trace()
                for ticker in stocks:
                    if not ticker in prices.keys():
                        prices[ticker] = {}
                    price = mt5_connection.get_symbol_info(ticker)
                    prices[ticker][price["time"]] = price
            date_as_str = date.today().strftime("%d%m%Y")
            path = "data/ticks/{}/".format(date_as_str)
            os.makedirs(path, exist_ok=True)
            for ticker in prices.keys():
                df_ticker = pd.DataFrame.from_dict(prices[ticker], orient="index")
                df_ticker.to_csv("{}/{}.csv".format(path, ticker))
            print(".")
            sleep(1)
if __name__ == "__main__":
    cli()
