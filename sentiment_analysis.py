#!/usr/bin/python3

import tweepy
from textblob import TextBlob
import sys

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

# make authentication variable
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API variable
api = tweepy.API(auth)

# word/phrase to be searched
search_phrase = sys.argv[1]

# create a list of searched tweets
public_tweets = api.search(search_phrase) # method retrieves bunch of tweets that contain the word Trump

# variables to measure sentiment polarity and subjectivity
net_polarity = 0
net_subjectivity = 0

for tweet in public_tweets:
    print(tweet.text) # print each tweet collected
    # create analysis variable
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

    net_polarity += analysis.sentiment.polarity
    net_subjectivity += analysis.sentiment.subjectivity

print("\n\n")
print("SENTIMENT ANALYSIS REPORT")
print("===========================")
print("Polarity [-1,1]: %.4f" %(net_polarity/len(public_tweets)))
print("Subjectivity [-1,1]: %.4f" %(net_subjectivity/len(public_tweets)))
print("\n\n")