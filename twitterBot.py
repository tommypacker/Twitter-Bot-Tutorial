import tweepy, time, sys
from tokens import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_SECRET, ACCESS_TOKEN

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

def printTimeLine():
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		print tweet.text
		print

def tweetSomething():
	tweetStatus = raw_input('Enter your tweet: ')
	api.update_status(tweetStatus)

while True:
	userOption = raw_input('Type p to print Timeline, t to tweet something, anything else to quit: ')
	if userOption == 'p':
		printTimeLine()
	elif userOption == 't':
		tweetSomething()
	else:
		break