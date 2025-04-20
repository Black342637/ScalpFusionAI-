import pandas_ta as ta

def calculate_indicators(df):
    df.ta.rsi(length=14, append=True)
    df.ta.macd(fast=12, slow=26, signal=9, append=True)
    df.ta.sma(length=9, append=True)
    df.ta.sma(length=21, append=True)
    return df
