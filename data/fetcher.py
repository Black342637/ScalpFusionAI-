import ccxt
import pandas as pd

def fetch_mexc_klines(symbol="BTC/USDT", timeframe="1m", limit=100):
    exchange = ccxt.mexc({"enableRateLimit": True})

    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        if not ohlcv or len(ohlcv[0]) < 6:
            raise ValueError("Brak danych OHLCV lub nieprawidłowy format")
        df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    except Exception as e:
        print(f"Błąd przy pobieraniu danych: {e}")
        return pd.DataFrame()  # pusty dataframe, by nie wywalić bota
 28d1b6f (Fix: updated imports to match src folder for Render)
