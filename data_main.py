from alchemyapi import AlchemyAPI
import json
from pprint import pprint
import calendar
from datetime import datetime
import data_count
import data_alchanalysis

class TweetInfo:
	def __init__(self, datetime, id, text):
		self.datetime = datetime
		self.id = id
		self.text = text
		self.hashtags = []
		self.attags = []
		self.sentiment = None
		self.responseEntities = None
		self.responseKeywords = None
		self.responseSentiment = None

def getTPM(arrOfObj):
	start = arrOfObj[0].datetime
	intervals = (arrOfObj[len(arrOfObj)-1].datetime-start)/300+1
	tweetPerMin = [0]*intervals
	
	for x in arrOfObj:
		secs = x.datetime - start
		tweetPerMin[int(secs/300)] += 1
	return tweetPerMin

def getNSPM(arrOfObj):
	start = arrOfObj[0].datetime
	intervals = (arrOfObj[len(arrOfObj)-1].datetime-start)/300+1
	negPerMin = [0]*intervals
	totPerMin = [1]*intervals
	
	for x in arrOfObj:
		secs = x.datetime - start
		totPerMin[int(secs/300)] +=1
		if(x.sentiment<0):
			negPerMin[int(secs/300)] +=1
	for y in range(0,intervals-1):
		negPerMin[y] = negPerMin[y]/totPerMin[y]
	return negPerMin
	
def getPSPM(arrOfObj):
	start = arrOfObj[0].datetime
	intervals = (arrOfObj[len(arrOfObj)-1].datetime-start)/300+1
	posPerMin = [0]*intervals
	totPerMin = [1]*intervals
	
	for x in arrOfObj:
		secs = x.datetime - start
		totPerMin[int(secs/300)] +=1
		if(x.sentiment>0):
			posPerMin[int(secs/300)] +=1
	for y in range(0,intervals-1):
		posPerMin[y] = posPerMin[y]/totPerMin[y]
	return posPerMin

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
	
def getPositiveSentiment(twitterarray):
	
	data_alchanalysis.getAlcData(twitterarray)
	for i in range(0, 100):
	#for i in range(0, len(twitterarray)):
		response = twitterarray[i].responseSentiment
		if response['status'] == 'OK':
			type = response['docSentiment']['type']
			print i
			print type + "\n"
			
			if type == 'positive':
				twitterarray[i].sentiment = 1
			elif type == 'neutral':
				twitterarray[i].sentiment = 0
			elif type == 'negative':
				twitterarray[i].sentiment = -1


		else:
			print('Error in sentiment analysis call: ', response['statusInfo'])
	

def main():
	
	data = 'test_data'
	tweetarray = getDatafromRaw(data)
	tpm = getTPM(tweetarray)

	formatted_data = toJSFM(tpm)
# 	print formatted_data
	print "Formated test data, Tweets per Minute"
	print getprocessedTPM('test_data')
	
#Set the HashTag and AtTag values in each object	
	for item in tweetarray:
		item.hashtags = data_count.getHashTags(item.text)
		item.attags = data_count.getAtTags(item.text)
	
	print
	print
	print "top 50 most common hashtags/@tags and their amount"
	print data_count.getCloud(tweetarray)
	print tweetarray[4].sentiment
	
	getPositiveSentiment(tweetarray)
	
#	positive = getPSPM(tweetarray)
# 	negative = getNSPM(tweetarray)
# 	
# 	print toJSFM(positive)
# 	print toJSFM(negative)
	
# WHAT YOU NEED TO DO
# FINISH IMPLEMENTING DATA_ALCHANALYSIS -- HAS NOT BEEN IMPLEMENTED IN THIS .PY YET
# PRINT OUT RELEVANT DATA FROM ALCHANALYSIS AND PUT INTO TXT FILE -- GIVE TO ADITYA
# DATA_COUNT IS GOOD. TWEETS PER MINUTE IS GOOD. JUST NEED POS/NEG FEEDBACK GRAPH
# Give Aditya 3 files - output (tpm), output2 (cloud data), output3 (alc feedback)
# output and output2 are already in the Lytix folder.
# also we're naming it Lytic.al
	
#for now just spitting out data for sake of having something written without front-end
	#data_alchanalysis.getAlcData(tweetarray)
	#getPositiveSentiment(tweetarray)
# 	for i in range(0, 50):
# 		data_alchanalysis.getEntities(tweetarray[i])
# 		data_alchanalysis.getKeywords(tweetarray[i])

	
if __name__ == '__main__':
	main() # test client
