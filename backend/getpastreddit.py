import pandas as pd
import requests
import json
import csv
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


def makeurl(start_time, end_time):
	URL = 'https://api.pushshift.io/reddit/search/submission/?'
	URL = URL + 'after=' + start_time +'&before=' + end_time + '&subreddit=wallstreetbets'
	return(URL)


def main(start, end):
	startd, endd = convertdates(start, end)
	print(startd)
	print(endd)
	url = makeurl(startd, endd)
	print(url)

main("01/1/2021","02/1/2021")
