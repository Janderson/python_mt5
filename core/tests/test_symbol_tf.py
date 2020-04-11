import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.symbol_tf import SymbolTF

def test_symbol_tf():
    symbol_tf = SymbolTF("PETR4", "D1")
    symbol_tf.symbol == "PETR4"
    symbol_tf.timeframe == "D1"
