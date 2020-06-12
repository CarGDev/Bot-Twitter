import tweepy
import time
from keys import keys
SCREEN_NAME = keys['screen_name']
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user =  api.me()

search = 'NuncaParesDeAprender'
lang = 'es'
nrTweets = 15

for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('He dado Like')
        tweet.favorite()
        time.sleep(50)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break