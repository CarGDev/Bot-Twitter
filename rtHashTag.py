import tweepy

from keys import keys

import time

SCREEN_NAME = keys['screen_name']
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)
print(SCREEN_NAME)

### Retweet the palabras clave
def main():
    search = input('A quien quieres darle retweet: ')
    # search = ("100DaysOfCode", "NuncaParesDeAprender", "anncode", "darkjeda", "zukiblue", "platzi", "coding", "javascript")
    numberofTweets = 5
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

main()