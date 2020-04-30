# Andrew M Kigara ©
# Feel free to try out this bot while I build other cool ones :)

# Briefly: This bot is only designed to like tweets based off 
# a *KEYWORD*

# Eg: Like all tweets with the name Pubg

import tweepy
import time

# Store your Keys and Tokens in a dictionary
# for easier access and readability
keys = dict(
consumer_key='Your API Key',
consumer_secret='Your API Secret Key',
access_token='Your Access Token',
access_token_secret='Your Secret Access Token'
)

# THE ***MAGIC***
auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

keyWord = "Your keyword here" # Keyword inside the quotes

limitTweets = 100 #Don't get banned lol

for tweet in tweepy.Cursor(api.search, keyWord).items(limitTweets):
    # Used Try-Catch to handle errors
    try:
        print("Tweet Liked") # Debug purposes
        tweet.favorite()
        time.sleep(100)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
