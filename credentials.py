import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'
access_token = 'your access token'
access_token_secret = 'your token secret'


def createInterface():
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    return tweepy.API(auth)
