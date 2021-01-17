import pandas as pd
import requests
import json
import csv
import time
import datetime
import threading

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
    try:
    	text = subm['selftext']
    except KeyError:
    	text=''

    awards = subm['total_awards_received']
    
    subData.append((sub_id,title, text, flair))
    subStats[sub_id] = subData


def updateSubs_file():
    upload_count = 0
    #location = "\\Reddit Data\\" >> If you're running this outside of a notebook you'll need this to direct to a specific location
    file = 'shot.csv'
    with open(file, 'w', newline='', encoding='utf-8') as file: 
        a = csv.writer(file, delimiter=',')
        headers = ["Post ID","Title", "text", "Flair"]
        a.writerow(headers)
        for sub in subStats:
            a.writerow(subStats[sub][0])
            upload_count+=1
            
        print(str(upload_count) + " submissions have been uploaded")
   

def main(startd, endd):
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
	print('Thread Done')


	return


def lightning(start, end, threads = 8):
	startd, endd = convertdates(start, end)
	intervailtime = (endd - startd) // threads
	thr = []
	for i in range(0, threads):
		t= threading.Thread( target=main, args=(startd + i*intervailtime, startd + i*intervailtime + intervailtime,))
		t.start()
		thr.append(t)

	for t in thr:
		t.join()
	updateSubs_file()
	return


lightning("30/1/2020","31/1/2020")









# Cntrl D exits vm
