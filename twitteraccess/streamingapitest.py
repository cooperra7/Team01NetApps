import tweepy
import twitteraccess

api = twitteraccess.get_twitter_api_handle()
myStreamListener = twitteraccess.MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

result = myStream.filter(track=['@team01netapp'], async=True)
print(result)

