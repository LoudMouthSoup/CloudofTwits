#! /home/mr/Git/Coudoftwits

import json
import os
import tweepy
from tweepy import OAuthHandler


def read_config(credentials):
		"""
		Currently pulling unencypted creditals. Need to go 
		back and figure out how to make this more secure
		""" 
		with open(credentials, 'r') as infile:
			credentials = json.load(infile)

		return(credentials)

credentials = read_config('/home/mr/Documents/creds/twitter_cred.json')
auth = OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_SECRET'])
api = tweepy.API(auth)

def return_recent_tweets(num):
	"""
	This returns the most recent tweets on your timeline.
	Enter the amount of tweets you would like to return.
	"""
	tweet_list = []
	for status in tweepy.Cursor(api.home_timeline).items(num):
	# process a single status
		tweet_list.append(status.text)
	return tweet_list

def store_recent_tweets(num):
	"""
	This stores the most recent tweets on your timeline into a json.
	Enter the amount of tweets you would like to return.
	"""
	for status in tweepy.Cursor(api.home_timeline).items(num):
	# process a single status
		store(status._json)

print(store_recent_tweets(10))





