# Script to scrape posts from reddit
import praw
def openreddit():
	'''
	Opens a instance of reddit
	Args- None
	Reurns - instance of reddit
	'''
	reddit = praw.Reddit(client_id='mWvbVCWHYUENwg', client_secret='19JmDSHqV-PpdJfFJ4YcB1YbibEWdw', user_agent='Reddit Webscrape')
	return(reddit)


def get_posts(reddit, date, filter, n):  # Todo make it so all posts from a day come back automatically
	'''
	Gets posts from reddit
	arg - reddit: instance of reddit
	Arg - Date: Date of posts
	arg - filter: How you want reddit to filter posts
	arg - n: Number of posts
	returns - List of posts
	'''
	hot_posts = reddit.subreddit('wallstreetbets').hot(limit=n)
	return(hot_posts)


def main():
	redditinstance = openreddit()
	posts = get_posts(redditinstance, 'hi', 'hi', 5)
	for post in posts:
		print(post.title)
	return

main()


