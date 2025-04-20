from data.fetcher import fetch_mexc_klines
from indicators.technical import calculate_indicators
import pandas as pd

def main():
    df = fetch_mexc_klines()
    df = calculate_indicators(df)
    print(df.tail())

if __name__ == "__main__":
    main()
