import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(  # noqa: E402 - Avoid flake8 error 402
    os.path.join(os.path.dirname(__file__), '../..'))
)
from commands.export_bars import ExportBars


class MockConnection:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    def get_bars_to_df(self, symbol_tf, qtd):
        print("---> thats great {}".format(symbol_tf))
        return pd.DataFrame()


def test_exportBars():
    export_bars_cmd = ExportBars(MockConnection())
    export_bars_cmd.parameters(symbols=["PETR4"],
                               timeframes=["D1"],
                               path="data",
                               bars=5000)
    export_bars_cmd.run()
    export_bars_cmd.result() == 0
