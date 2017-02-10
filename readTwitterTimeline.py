import tweepy

consumer_key = '2D09LEUICkWMvLgZauponx0PP'
consumer_secret = 'WHudhytJ88G1LizV5US7LS2yBKo9tIG32CKiXsvBr4JL5atbpk'
access_token = '828655445250289664-eyKXFCeEJwmWDeeVdVLbPy1CwtqzRRp'
access_token_secret = 'rRvtRknM2UdTtVdQqITwuGyDeX2caviTpswg67NGDgarN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Send a public tweet to timeline
# api.update_status('Update status test #2')

# Read public tweets from timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
