from alchemyapi import AlchemyAPI
import json
from pprint import pprint
import calendar
from datetime import datetime
import data_count

class TweetInfo:
	def __init__(self, datetime, id, text):
		self.datetime = datetime
		self.id = id
		self.text = text
		self.hashtags = []
		self.attags = []

def getTPM(arrOfObj):
	start = arrOfObj[0].datetime
	intervals = (arrOfObj[len(arrOfObj)-1].datetime-start)/300+1
	tweetPerMin = [0]*intervals
	for x in range(0, len(tweetPerMin)):
		tweetPerMin[x] = 0
	for x in arrOfObj:
		secs = x.datetime - start
		tweetPerMin[int(secs/300)] += 1
	return tweetPerMin


def getDatafromRaw(rawdata):
	with open(rawdata) as f:
		data = json.loads(f.read())
    	datArr = []
    

    	for item in data:		
			s = item["created_at"]
			t = calendar.timegm(datetime.strptime(s, "%a %b %d %H:%M:%S +0000 %Y").timetuple())
			
			id = item["id"]
			text = item["text"]
				
			tInf = TweetInfo(t, id, text)
			datArr.append(tInf)
		
	return datArr

def toJSFM(convert):
	converted = "["
	for i in range(0, len(convert)): 					#Parses through the string you want to convert
		converted += "[" + str(i*5) + ", " + str(convert[i]) + "]"	#Formats it
		if(i < len(convert)-1):
			converted += ", "					#Checks for last entry to determine if it should
		else:								#end with ", " or "]"
			converted += "]"

	#print converted
	return converted
	

def getprocessedTPM(data):

	tweetarray = getDatafromRaw(data)
	tpm = getTPM(tweetarray)

	return toJSFM(tpm)

def main():
	
# 	print "tae-min's part"
	data = 'test_data'
	tweetarray = getDatafromRaw(data)
	tpm = getTPM(tweetarray)
	
# 	print "-----------------------------\n"
# 	
# 	print "felix's part"
	formatted_data = toJSFM(tpm)
# 	print formatted_data
	print getprocessedTPM('test_data')

	print data_count.getCloud(tweetarray)
	
	
	
	

	
if __name__ == '__main__':
	main() # test client