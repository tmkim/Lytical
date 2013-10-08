from alchemyapi import AlchemyAPI
import json
from pprint import pprint
import calendar
from datetime import datetime

alchemyapi = AlchemyAPI()

class TweetInfo:
	def __init__(self, datetime, id, text):
		self.datetime = datetime
		self.id = id
		self.text = text


#  pass the array of tweetinfo objects to countTPM	
def countTPM(tweetarray):
	timeincrement = 300
	countreply = []
	i = 0
	
#  Parameter is array of objects, return "tweetPerMin[]" 0 = <5min, 1 = 5-10min, 2 = 10-15, etc
def getTPM(arrOfObj):
	start = arrOfObj[0].datetime
	intervals = (arrOfObj[len(arrOfObj)-1].datetime-start)/300+1
	tweetPerMin = [0]*intervals
	for x in range(0, len(tweetPerMin)):
		tweetPerMin[x] = 0
	print(len(tweetPerMin))
	for x in arrOfObj:
		secs = x.datetime - start
		print(secs)
		tweetPerMin[int(secs/300)] += 1
	return tweetPerMin



	for x in range(0,len(tweetarray)):
		if tweetarray[x].time % timeincrement == 0:
			countreply[i] += 1
			i += 1
		
		if tweetarray[x].time % timeincrement != 0:
			countreply[i] += 1
	
	for x in range(0, length(countreply)):
		print countreply[x]


def main():
    with open('test_data') as f:
        data = json.loads(f.read())
	datArr = []
	for item in data:		
		s = item["created_at"]
		t = calendar.timegm(datetime.strptime(s, "%a %b %d %H:%M:%S +0000 %Y").timetuple())
			
		id = item["id"]
		text = item["text"]
			
		tInf = TweetInfo(t, id, text)
		datArr.append(tInf)
	
	for x in range(0,len(datArr)):
		print (datArr[x].datetime)

	tpmz = getTPM(datArr)

	for x in range(0,len(tpmz)):
		print(tpmz[x])
	

	countTPM(datArr)
	
if __name__ == '__main__':
	main()
