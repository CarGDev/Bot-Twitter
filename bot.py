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
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)

### Seguir a quien me sigue
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("acabo de seguir a ")
    print (follower.screen_name)
    time.sleep(50)

### Retweet the palabras clave
def main():
    search = ("@cargdev" )

    numberofTweets = 1
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
# main()