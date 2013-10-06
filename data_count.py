from alchemyapi import AlchemyAPI
import json
from pprint import pprint
import calendar
from datetime import datetime
from collections  import Counter


#alchemyapi = AlchemyAPI()
class TweetInfo:
 	def __init__(self, datetime, id, text):
 		self.datetime = datetime
 		self.id = id
 		self.text = text
 		self.hashtags = []
 		self.attags = []
 		
#  pass the array of tweetinfo objects to countTPM	
def countTPM(tweetarray):
	timeincrement = 300
	countreply = []
	i = 0
	
#  pass the string you want to search, get a string array of hashtags
def getHashTags(text):
	indices = findIndices(text,'#')
	tags = []
	for x in range(0,len(indices)):
		ind = indices[x]+1
		ind2 = ind
		while(text[ind2].isalpha()):
			ind2+=1
			if(ind2 == len(text)): 
				break
		tags.append(text[ind:ind2])
	return tags

#  pass the string you want to search, get a string array of at tags
def getAtTags(text):
	indices = findIndices(text,'@')
	tags = []
	for x in range(0,len(indices)):
		ind = indices[x]+1
		ind2 = ind
		while(text[ind2].isalpha()):
			ind2+=1
			if(ind2 == len(text)): 
				break
		tags.append(text[ind:ind2])
	return tags

#  pass the string you want to search and char c you want to search for, get an int array of indices where char c is
def findIndices(s,c):
	return [i for i, ltr in enumerate(s) if ltr == c]

#  pass the array of data you want to count words for, returns a single list of every word and how many times the word was used (sorted by # of time used)
def tagCounter(arrayOfData):
	taglist=[]
	for item in arrayOfData:
		for word in item.hashtags:
			taglist.append(word)
		for word in item.attags:
			taglist.append(word)
	cnt = Counter()
	for word in taglist:
		cnt[word] += 1
	return cnt

#  pass the array of data you want counted, returns the 50 most common tags
def getCloud(datArr):
	count = tagCounter(datArr)
	return count.most_common(50)

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



# 	for x in range(0,len(tweetarray)):
# 		if tweetarray[x].time % timeincrement == 0:
# 			countreply[i] += 1
# 			i += 1
# 		
# 		if tweetarray[x].time % timeincrement != 0:
# 			countreply[i] += 1
# 	
# 	for x in range(0, length(countreply)):
# 		print countreply[x]


def main():
    with open('test_data') as f:
        data = json.loads(f.read())
	datArr = []
	for item in data:		
		s = item["created_at"]	
		t = calendar.timegm(datetime.strptime(s, "%a %b %d %H:%M:%S +0000 %Y").timetuple()) #convert datetimestamp to unix time
			
		id = item["id"]
		text = item["text"]
			
		tInf = TweetInfo(t, id, text)
		tInf.hashtags = getHashTags(tInf.text)
		tInf.attags = getAtTags(tInf.text)
		datArr.append(tInf)
	
	print(getCloud(datArr))
	
if __name__ == '__main__':
	main()
