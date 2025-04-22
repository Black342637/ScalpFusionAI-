def calculate_ai_score(rsi, macd, ma_fast, ma_slow):
    score = 0

    # RSI - neutralny = 50
    if rsi < 30:
        score += 30
    elif rsi > 70:
        score -= 30
    else:
        score += 10

    # MACD
    if macd > 0:
        score += 25
    else:
        score -= 25

    # MA - przeciecie
    if ma_fast > ma_slow:
        score += 25
    else:
        score -= 10

    confidence = max(0, min(100, 50 + score))
    return confidence, score
