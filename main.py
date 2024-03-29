from core.symbol_tf import SymbolTF
from commands.export_bars import ExportBars
from market_data.mt5.mt5_converter import MT5Converter
from market_data.mt5.mt5_connection import MT5Connection
from time import sleep
from datetime import date
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
@click.option('timeframes', '--timeframes', default="D1", help='TimeFrame to export.')
@click.option('tickers', '--tickers', default="PETR4",  help='Stocks to export.')
def export_bars(bars, timeframes, tickers):
    timeframes = timeframes.split(",")
    tickers = tickers.split(",")
    with MT5Connection() as mt5_connection:
        exportbars_cmd = ExportBars(MT5Converter(mt5_connection))
        exportbars_cmd.parameters(tickers = list(tickers), 
                                  timeframes = list(timeframes), bars=bars)
        exportbars_cmd.run()


@cli.command('monitor_ticks')
@click.argument('tickers', default="BOVA11,PETR3")
def monitor_ticks(tickers):
    tickers = tickers.split(",")
    print(f"monitorando: {tickers}")
    prices={}
    for i in range(105000):
            with MT5Connection() as mt5_connection:
                for ticker in tickers:
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
