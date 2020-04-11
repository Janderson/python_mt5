from core.symbol_tf import SymbolTF
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
@click.option('--time_frame', default="D1", help='TimeFrame to export.')
def export_bars(bars, qtd_loop, time_frame):
    stocks = ["WIN$N", "BOVA11", "FESA4", "OIBR3", "PETR4"]
    data={}
    for i in range(qtd_loop):
        with MT5Connection() as mt5_connection:
            #print(mt5.version())
            mt5 = MT5Converter(mt5_connection)
            for stock in stocks:
                print ("exporting bars of {}-->".format(stock))
                try:
                    print("");#mt5_connection.get_ticks(stock, (datetime.today() - timedelta(hours=1)), 100))
                except Exception as e:
                    print("error e: {}".format(e))
                    import traceback
                    traceback.print_exc()
                try:
                    bars_df = mt5.get_bars_to_df(SymbolTF(stock, time_frame), qtd=bars)
                except Exception as e:
                    print("error e: {}".format(e))
                    import traceback
                    traceback.print_exc()
                #import ipdb; ipdb.set_trace()
                bars_df.to_csv("data/{}_{}.csv".format(stock, time_frame))
            if qtd_loop>1 or qtd_loop!=0:
                sleep(5)

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
