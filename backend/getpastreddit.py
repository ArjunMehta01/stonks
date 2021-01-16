import pandas as pd
import requests
import json
import csv
import time
import datetime

subStats = {}

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


def makeurl(start_time, end_time):
	URL = 'https://api.pushshift.io/reddit/search/submission/?'
	URL = URL + 'after=' + str(int(start_time)) +'&before=' + str(int(end_time)) + '&subreddit=wallstreetbets'
	return(URL)


def getPushshiftData(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']


def collectSubData(subm):
	#  WANTS, Score, title, text
    subData = list() #list to store data points
    title = subm['title']
    url = subm['url']
    try:
        flair = subm['link_flair_text']
    except KeyError:
        flair = "NaN"    
    author = subm['author']
    sub_id = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc']) #1520561700.0
    numComms = subm['num_comments']
    permalink = subm['permalink']
    text = subm['selftext']
    awards = subm['total_awards_received']
    upvoteratio = subm['upvote_ratio']
    
    subData.append((sub_id,title, text, url,author,score, upvoteratio, created,numComms,permalink,flair, awards))
    subStats[sub_id] = subData
   

def main(start, end):
	startd, endd = convertdates(start, end)
	print(startd)
	print(endd)
	url = makeurl(startd, endd)
	print(url)
	submissions = []
	data = getPushshiftData(url)
	subcount = 0
	while len(data) > 0:
		print(len(data))
		for submission in data:
			collectSubData(submission)
			subcount += 1
		print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
		print('ping') # Remove
		after = data[-1]['created_utc']
		url = makeurl(after, endd)
		data = getPushshiftData(url)
	print(str(len(subStats)) + " submissions have added to list")
	print("1st entry is:")
	print(list(subStats.values())[0][0][1] + " created: " + str(list(subStats.values())[0][0][5]))
	print("Last entry is:")
	print(list(subStats.values())[-1][0][1] + " created: " + str(list(subStats.values())[-1][0]))
	return

main("01/1/2021","02/1/2021")
