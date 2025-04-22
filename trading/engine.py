def decision_logic(row):
    if row["MA_fast"] > row["MA_slow"] and row["RSI_14"] < 30:
        return "BUY"
    elif row["MA_fast"] < row["MA_slow"] and row["RSI_14"] > 70:
        return "SELL"
    else:
        return "HOLD"
