import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def create_api():
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_SECRET"),
    )
    return tweepy.API(auth)

def post_tweet(content):
    api = create_api()
    api.update_status(status=content)
