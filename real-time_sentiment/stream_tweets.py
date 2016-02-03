import tweepy
# import json

# my keys
consumer_token = 'JqyH4BF9JozhYgAXYoljbWw8H'
consumer_secret = 'At0dRtyjqHIvJJtI32nggqwzAiWG25TEVHfe7QsR9LBIvs425c'
key = '1318985240-yYIz4hVWNmbvbpNeMvRkPNPIwxjCO2XqFOb4leQ'
secret = 'FBteOpkARK8kN3dpy6aVk3qgQMaKA7OC2xDsyDxU5pmjz'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
api.verify_credentials()


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_data(self, twitter_data):
        print(twitter_data)
        # tweetJSON = json.loads(twitter_data)
        # print(tweetJSON['text'].encode("utf-8"))


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

myStream.sample(async=False, languages=['en'])
