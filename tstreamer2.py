#! /home/mr/Git/Coudoftwits

import json
import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import twittercred

#api = tweepy.API(auth)

#def read_config(credentials):
	#"""
	#Currently pulling unencypted creditals. Need to go 
	#back and figure out how to make this more secure
	#""" 
	#with open(credentials, 'r') as infile:
	#	credentials = json.load(infile)

	#return(credentials)

#def return_recent_tweets(num):
"""
	This returns the most recent tweets on your timeline.
	Enter the amount of tweets you would like to return.
"""
	#tweet_list = []
	#for status in tweepy.Cursor(api.home_timeline).items(num):
	# process a single status
	#	tweet_list.append(status.text)
	#return tweet_list

#def store_recent_tweets(num):
"""
	This stores the most recent tweets on your timeline into a json.
	Enter the amount of tweets you would like to return.
"""
	#for status in tweepy.Cursor(api.home_timeline).items(num):
	# process a single status
	#store(status._json)

class TwitterStreamer():
	"""
	Class for streaming and processing live tweets
	"""
	def stream_tweets(self, fetched_tweets_filename, hashtag_list):
	# this handles twiiter authentication and connection to the twitter
	# streaming API 	
		listener = StdOutListener()
		auth = OAuthHandler(twittercred.CONSUMER_KEY, twittercred.CONSUMER_SECRET)
		auth.set_access_token(twittercred.ACCESS_TOKEN, twittercred.ACCESS_SECRET)

		stream = Stream(auth, listener)

		# keyword filter that adds items in track[] to the stream
		stream.filter(track=[hashtag_list])


class StdOutListener(StreamListener):
	"""
	A basic listener class that prints received tweets to stdout
	"""
	def __init__(self, fetched_tweets_filename):
		self.fetched_tweets_filename = fetched_tweets_filename

	def on_data(self, data):
		try:
			print(data)
			# a stands for append the file
			# what does tf stand for???
			with open(self.fetched_tweets_filename, 'a') as tf:
				tf.write(data)
			return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		print(status)


if __name__ == "__main__":
	hashtag_list = ['python', 'bitcoin', 'programing']
	fetched_tweets_filename = "tweets.json"

	twitter_streamer = TwitterStreamer
	twitter_streamer.stream_tweets(fetched_tweets_filename, hashtag_list)
	












