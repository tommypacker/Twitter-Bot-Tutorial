import tweepy, time, sys
from tokens import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_SECRET, ACCESS_TOKEN

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

def printTimeLine():

def tweetSomething():

while True:
	if userOption == 'p':
		printTimeLine()
	elif userOption == 't':
		tweetSomething()
	else:
		break
