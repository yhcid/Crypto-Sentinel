import tweepy
import os

class TwitterScraper:
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
            wait_on_rate_limit=True
        )
    
    def get_recent_tweets(self, symbol: str, limit=100):
        query = f"({symbol} OR ${symbol}) lang:en -is:retweet"
        response = self.client.search_recent_tweets(
            query=query,
            max_results=limit,
            tweet_fields=["created_at", "public_metrics"]
        )
        return [tweet.text for tweet in response.data]