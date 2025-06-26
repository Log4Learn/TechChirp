from utils import data_loader, tweet_generator, twitter_client, history_tracker

data = data_loader.load_subsidy_data("data/tips.xlsx")

for _, row in data.iterrows():
    theme = row.get("テーマ", "")
    content = row.get("内容", "")
    title_key = f"{theme}-{content[:20]}"  # 簡易一意識別

    if history_tracker.is_posted(title_key):
        continue

    tweet = tweet_generator.create_tweet(row)

    try:
        twitter_client.post_tweet(tweet)
        history_tracker.record_post(title_key)
        break  # 1投稿で終了
    except Exception as e:
        print(f"投稿失敗: {e}")
