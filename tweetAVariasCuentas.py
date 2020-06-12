import tweepy, sys, time
from random import randint
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

usuarios = sys.argv[1]
f = open(usuarios, "r")
h = f.readlines()
f.close()

for i in h:
    i = i.rstrip()
    m = i + " " + sys.argv[2]
    s = api.update_status(m)
    nap = randint(1, 60)
    time.sleep(nap)