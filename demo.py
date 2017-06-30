#!/usr/bin/python3

import tweepy
from textblob import TextBlob

consumer_key = 'lf2H9LleaedoyZH9MPfUTaFAV'
consumer_secret = 'SSCRSUBnxLRi9KjSrqJKy4XkLDD8WYqTfExYCSuqNPksKQgLF2'

access_token = '2581789579-0M0P48FFLrJsxI4TJdpBU4Ji4tdv7VT8gJErfN1'
access_token_secret = 'QmAKEyWIZLMpcmgpfHGRCJLEWd0m2im1XSRLGiZk8dx8Q'

# make authentication variable
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API variable
api = tweepy.API(auth)

# create a list of searched tweets
public_tweets = api.search('Trump') # method retrieves bunch of tweets that contain the word Trump

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