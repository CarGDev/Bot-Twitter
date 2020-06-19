import tweepy, sys, time

from random import randint
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


def users():
    usuarios = ["@CarGDev"]
    for follower in tweepy.Cursor(api.followers).items():
        try:
            user = "@" + follower.screen_name
            print(user)
            usuarios.append(user)
            # print (follower.screen_name)
            # i = i + 1
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        # print(time.ctime())
        time.sleep(5)
    # print(usuarios)
    return usuarios

f = users()
# print(f)

h = sys.argv[1]
text = open(h,"r")
textRead = text.readlines()
text.close
textRead = '  '.join(textRead)
# print(textRead)

for i in f:
    try:
        i = i.rstrip()
        m = i + textRead
        s = api.update_status(m)
        # print(m)
        print("Tweet to " + i)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

    nap = randint(1, 60)
    time.sleep(nap)

