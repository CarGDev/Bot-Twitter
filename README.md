# Bot-Twitter
Bot for retweet

This bot is for training with API in twitter.

1. The page for Twitter is [APPDeveloper](https://developer.twitter.com/en/apps)

2. First to all you have install **Tweepy** in python the documentation is in this [link](http://docs.tweepy.org/en/latest/)

## Installation
The easiest way to install the latest version from PyPI is by using pip:

`pip install tweepy`

You can also use Git to clone the repository from GitHub to install the latest development version:

`git clone https://github.com/tweepy/tweepy.git`  
`cd tweepy`  
`pip install .`

Alternatively, install directly from the GitHub repository:

`pip install git+https://github.com/tweepy/tweepy.git`

## Getting started
### Introduction

If you are new to Tweepy, this is the place to begin. The goal of this tutorial is to get you set-up and rolling with Tweepy. We won’t go into too much detail here, just some important basics.

`Hello Tweepy`
`import tweepy`

`auth = tweepy.OAuthHandler(consumer_key,consumer_secret)`
`auth.set_access_token(access_token, access_token_secret)`

`api = tweepy.API(auth)`

`public_tweets = api.home_timeline()`
`for tweet in public_tweets:`
`    print(tweet.text)`

This example will download your home timeline tweets and print each one of their texts to the console. Twitter requires all requests to use OAuth for authentication. The Authentication Tutorial goes into more details about authentication.

## Create Keys

for create the file Key copy the code below and save as **keys.py**

`keys = dict(`
`    screen_name = 'Your user without @',`
`    consumer_key =          '',`
`    consumer_secret =       '',`
`    access_token =          '',`
`    access_token_secret =   '',`
`)`