__name__ = "twitteraccess"
__author__ = "sarah.kharimah"

import tweepy
import json

"""
Create class MyStreamListener inheriting from StreamListener to listen to stream and print status text.

:param: None
:return: None

"""


class MyStreamListener(tweepy.StreamListener):

    counter = 0
    text = ''

    def on_status(self, status):
        print(status.text)

    def on_data(self, raw_data):
        data_in_json = json.loads(raw_data)
        self.counter = self.counter + 1
        print(data_in_json['text'])
        if self.counter > 0:
            self.text = data_in_json['text']
            send_tweet_to_timeline(get_twitter_api_handle(), data_in_json['text'])
            return False


"""
Authenticate OAuth authentication and get a tweepy API handle.

:param: None
:return: tweepy.API handle to access twitter API if successfully authenticated; None otherwise

"""


def get_twitter_api_handle():

    consumer_key = '2D09LEUICkWMvLgZauponx0PP'
    consumer_secret = 'WHudhytJ88G1LizV5US7LS2yBKo9tIG32CKiXsvBr4JL5atbpk'
    access_token = '828655445250289664-eyKXFCeEJwmWDeeVdVLbPy1CwtqzRRp'
    access_token_secret = 'rRvtRknM2UdTtVdQqITwuGyDeX2caviTpswg67NGDgarN'

    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except Exception as err:
        print(err)
        print('Unable to generate a Twitter API handle')
        return None


"""
Read the most recent tweet on the public timeline.
Print the newest status message on public Twitter timeline to the console.

:param: api_handle: (tweepy.API) tweepy API handle to access Twitter API
:return: (String) the most recent tweet if successful; None otherwise

"""


def get_most_recent_tweet(api_handle):
    recent_tweet = None
    try:
        public_tweets = api_handle.home_timeline()
        for tweet in public_tweets:
            recent_tweet = tweet.text
        print(recent_tweet)
        return recent_tweet
    except Exception as err:
        print(err)
        print('Unable to read the most recent tweet')
        return None


"""
Post a new status message to a public Twitter timeline.
Print the newest status message on public Twitter timeline to the console.

:param: api_handle: (tweepy.API) tweepy API handle to access Twitter API
:param: new_status_message: (String) status message to send to the timeline
:return: True if successfully post a new message to Twitter timeline; False otherwise

"""


def send_tweet_to_timeline(api_handle, new_status_message):

    try:
        api_handle.update_status(new_status_message)
        print('Tweeted successfully')
        return True
    except Exception as err:
        print(err)
        print('Unable to update status message')
        return False

