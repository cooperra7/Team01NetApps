import tweepy
import json
import twitteraccess

consumer_key = '2D09LEUICkWMvLgZauponx0PP'
consumer_secret = 'WHudhytJ88G1LizV5US7LS2yBKo9tIG32CKiXsvBr4JL5atbpk'
access_token = '828655445250289664-eyKXFCeEJwmWDeeVdVLbPy1CwtqzRRp'
access_token_secret = 'rRvtRknM2UdTtVdQqITwuGyDeX2caviTpswg67NGDgarN'

api = twitteraccess.get_twitter_api_handle()
myStreamListener = twitteraccess.MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

result = myStream.filter(track=['taylor swift'])

myStream.disconnect()
