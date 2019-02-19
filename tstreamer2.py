#! /home/mr/Git/Coudoftwits

import json
import os
import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import re

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

#### TWITTER CLIENT ####
class TwitterClient():
	def __init__(self, twitter_user=None):
		self.auth = TwitterAuthenticator().authenticate_twitter_app()
		self.twitter_client = API(self.auth)
		self.twitter_user = twitter_user

	def get_twitter_client_api(self):
		return self.twitter_client

	def get_user_timeline_tweets(self, num_tweets):
		user_timeline_tweets = []
		"""
		Cursor is the class that allows us to get the user timeline tweets
		Arguments
		user_timeline allows you to specify the user you want to collect tweets from
		if you do not specify anything, the default is your own timeline.
		id=self.twitter_user allows you to specify the user's timeline
		.items is a parameter for the Cursor object that specifies the number
		of tweets to collect. This has been set to an argument of the function.
		"""
		for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
			user_timeline_tweets.append(tweet)
			return user_timeline_tweets 

	def get_followers(self, num_followers):
		followers = []
		for followers in Cursor(self.twitter_client.followers, id=self.twitter_user).items(num_followers):
			followers.append(followers)
			return followers

	def get_friend_list(self, num_friends):
		friend_list = []
		for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
			friend_list.append(friend)
			return friend_list

	def get_home_timeline_tweets(self, num_tweets):
		home_timeline_tweets = []
		for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
			home_timeline_tweets.append(tweet)
			return home_timeline_tweets

#### TWITTER AUTHENTICATOR #####
class TwitterAuthenticator():

	def authenticate_twitter_app(self):
		auth = OAuthHandler(twittercred.CONSUMER_KEY, twittercred.CONSUMER_SECRET)
		auth.set_access_token(twittercred.ACCESS_TOKEN, twittercred.ACCESS_SECRET)
		return auth


##### TWITTER STREAMER ######
class TwitterStreamer():
	"""
	Class for streaming and processing live tweets
	"""
	def __init__(self):
		self.twitter_authenticator = TwitterAuthenticator()

	def stream_tweets(self, fetched_tweets_filename, hashtag_list):
	# this handles twitter authentication and connection to the twitter
	# streaming API 	
		listener = TwitterListener(fetched_tweets_filename)
		auth = self.twitter_authenticator.authenticate_twitter_app()
		stream = Stream(auth, listener)


		# keyword filter that adds items in track[] to the stream
		stream.filter(track=hashtag_list)

##### TWITTER STREAM LISTENER #######
class TwitterListener(StreamListener):
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
		if status == 420:
			# Returning False on_data method in case rate limit occurs
			# not killing the process could result in being kicked out of
			# API by twitter
			return False
		print(status)

class TweetAnalyzer():
	"""
	Functionality for analyzing and categorizing content from tweets
	"""
	
	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def analyze_sentiment(self, tweet):
		analysis = TextBlob(self.clean_tweet(tweet))

		if analysis.sentiment.polarity > 0:
			return 1
		elif analysis.sentiment.polarity == 0:
			return 0
		else:
			return -1


	def tweets_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		# feeds in a numpy array and creates a column named id
		df['ID'] = np.array([tweet.id for tweet in tweets])
		df['Liked'] = np.array([tweet.favorite_count for tweet in tweets])
		df['Retweeted'] = np.array([tweet.retweet_count for tweet in tweets])
		df['Text'] = np.array([tweet.text for tweet in tweets])
		df['Length'] = np.array([len(tweet.text) for tweet in tweets])
		df['Date'] = np.array([tweet.created_at for tweet in tweets])
		df['Source'] = np.array([tweet.source for tweet in tweets])

		return df


if __name__ == "__main__":
	twitter_client = TwitterClient()
	api = twitter_client.get_twitter_client_api()
	tweet_analyzer = TweetAnalyzer()
	tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)
	
	df = tweet_analyzer.tweets_to_data_frame(tweets)
	df['Sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])

	print(df.head(10))
 

	
	# Get the average length over all tweets
	#print(np.mean(df['Length']))

	# Get the number of likes for the tweet that received the most likes
	#print(np.max(df['Favorited']))

	# Get the number of retweets for the tweet that received the most retweets
	#print(np.max(df['Retweeted']))
	

	# Time Series graph for Likes
	#time_likes = pd.Series(data=df['Liked'].values, index=df['Date'])
	#time_likes.plot(figsize=(16, 4), color='r')
	#plt.show()

	# Time Series graph for Retweets
	#time_retweets = pd.Series(data=df['Retweeted'].values, index=df['Date'])
	#time_retweets.plot(figsize=(16, 4), color='b')
	#plt.show()

	# Time Series graph for Retweets & Likes
	# color is optional because colores will be auto assigned
	#time_retweets = pd.Series(data=df['Retweeted'].values, index=df['Date'])
	#time_retweets.plot(figsize=(16, 4), label='Likes', legend=True, color='b')
	#time_likes = pd.Series(data=df['Liked'].values, index=df['Date'])
	#time_likes.plot(figsize=(16, 4), label='Retweets', legend=True, color='r')
	#plt.show()

	#print(df.head(10))
	
	# print(dir(tweets[0])) gives a list of types of information you can extract from the tweet
	# add the data type after tweet
	#print(tweets[0].id)
	#print(tweets[0].geo)
	#print(tweets[0].place)
	#print(tweets[0].retweet_count)



#if __name__ == "__main__":
#	hashtag_list = ['python', 'bitcoin', 'programing']
#	fetched_tweets_filename = "tweets.json"
	# here we can pass the name of the @user
#	twitter_client = TwitterClient('justinnevins_')
	#print(twitter_client.get_user_timeline_tweets(1))
#	print(twitter_client.get_friend_list(50))


#	twitter_streamer = TwitterStreamer()
#	twitter_streamer.stream_tweets(fetched_tweets_filename, hashtag_list)
	












