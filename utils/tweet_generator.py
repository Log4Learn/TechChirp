def create_tweet(entry):
    theme = entry.get("テーマ", "").strip()
    content = entry.get("内容", "").strip()
    return f"【{theme}】{content} #エンジニア #技術メモ"[:280]
