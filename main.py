import tweepy
from tweepy import OAuthHandler
from user_information import consumer_key, consumer_secret, access_secret, access_token
"""
Make sure you have user_information.py file that includes this:

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
"""
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


api = tweepy.API(auth)


if __name__ == "__main__":
    api

#######
 
