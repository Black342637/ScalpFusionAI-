
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
