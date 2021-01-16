# Script to scrape posts from reddit
import praw
import time
import datetime


def convertdates(start_date, end_date):
	'''
	Converts a D/M/Y time to a UNix timecode
	Example (D/M/Y = "01/12/2011")
	args - start/end date: Date of start / end of reddit search (D/M/Y)
	retuns - start/end date unix: Start/ end date of reddit search in unix timecode
	'''
	unixstart = time.mktime(datetime.datetime.strptime(start_date, "%d/%m/%Y").timetuple())
	unixend = time.mktime(datetime.datetime.strptime(end_date, "%d/%m/%Y").timetuple())
	return(unixstart, unixend)


def openreddit():
	'''
	Opens a instance of reddit
	Args- None
	Reurns - instance of reddit
	'''
	reddit = praw.Reddit(client_id='mWvbVCWHYUENwg', client_secret='19JmDSHqV-PpdJfFJ4YcB1YbibEWdw', user_agent='Reddit Webscrape')
	return(reddit)


def get_posts(reddit, start_date, end_date, n=0):  # Todo make it so all posts from a day come back automatically
	'''
	Gets posts from reddit
	arg - reddit: instance of reddit
	Arg - start_ate: Start date of post in unix time code
	arg - end_date: End date of posts in unix timecode
	arg - n: Number of posts
	returns - List of posts
	'''
	posts = []
	for submission in reddit.subreddit('wallstreetbets').submissions(start_date, end_date):
		posts += [submission]
	return(posts)


def main(start, end):
	redditinstance = openreddit()
	startd, endd = convertdates(start, end)  # Gets Unix start and end dates for reddit search
	print(startd)
	print(endd)
	# TEMP after this
	posts = get_posts(redditinstance, startd, endd)
	for post in posts:
		print(post.title)
	return

main("01/1/2021","02/1/2021")
