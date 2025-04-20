import ccxt
import pandas as pd

def fetch_mexc_klines(symbol="BTC/USDT", timeframe="1m", limit=100):
    exchange = ccxt.mexc({"enableRateLimit": True})
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df
