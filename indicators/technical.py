import pandas as pd

def calculate_indicators(df):
    # RSI
    delta = df["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df["RSI_14"] = 100 - (100 / (1 + rs))

    # MA
    df["MA_fast"] = df["close"].rolling(window=9).mean()
    df["MA_slow"] = df["close"].rolling(window=21).mean()

    # MACD
    ema12 = df["close"].ewm(span=12, adjust=False).mean()
    ema26 = df["close"].ewm(span=26, adjust=False).mean()
    df["MACD_12_26_9"] = ema12 - ema26

    return df
