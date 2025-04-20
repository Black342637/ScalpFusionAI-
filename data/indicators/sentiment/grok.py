def get_grok_sentiment(token):
    """
    Mock funkcji sentymentu od Groka (zastępcza odpowiedź).
    W przyszłości można podpiąć API Groka lub alternatywy.
    """
    return {
        "sentiment": 0.7,  # -1 do 1
        "volume_change": 1.2,
        "news_impact": "neutral"
    }
