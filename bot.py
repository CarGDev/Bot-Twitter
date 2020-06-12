import tweepy
import os
os.chdir("./keys.py")

auth = tweepy.OAuthHandler (os.consumer_key, os.consumer_secret)
auth.set_access_token (os.access_token, os.access_token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
  search = ("python","coding","NUNCAPARESDEAPRENDER")
  numberOfTweets = 5
  for tweet in tweepy.Cursor(api.search).items(numberOfTweets):
    try:
      tweet.retweet()
      print("Tweet Retweeted")
    except tweepy.TweepError as e:
      print(e.reason)
    except StopIteration:
      break

main()