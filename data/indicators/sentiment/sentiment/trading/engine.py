def decision_logic(row):
    """
    Prosty silnik decyzyjny na podstawie wskaźników:
    - RSI poniżej 30 i MACD rośnie = BUY
    - RSI powyżej 70 i MACD maleje = SELL
    - Inaczej: HOLD
    """
    rsi = row.get("RSI_14")
    macd = row.get("MACD_12_26_9")
    macd_signal = row.get("MACDs_12_26_9")

    if rsi is None or macd is None or macd_signal is None:
        return "HOLD"

    if rsi < 30 and macd > macd_signal:
        return "BUY"
    elif rsi > 70 and macd < macd_signal:
        return "SELL"
    else:
        return "HOLD"
