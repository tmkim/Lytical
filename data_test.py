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


def main():
	with open('test_data') as f:
		data = json.loads(f.read())
        
	datArr = []
	for item in data:
		date = item["created_at"][4:10]
		mon = monToNum(date[0:3])
		date = str(mon) + " " + str(date[4:7])
		time = item["created_at"][11:19]
		time = timeToSec(time)
		id = item["id"]
		text = item["text"]
		
		tInf = TweetInfo(date, time, id, text)
		datArr.append(tInf)
	
	#for x in range(0,100):
	for x in range(0,len(datArr)):
		print (datArr[x].time)

	#countTPM(datArr)
	
	for x in range(0,10):
	#for x in range(0,len(datArr)):
		response = alchemyapi.entities('text',datArr[x].text, { 'sentiment':1 })	
		if response['status'] == 'OK':
			for entity in response['entities']:
				print datArr[x].text
				print 'text: ' + entity['text']
				print 'type: ' + entity['type']
				print 'relevance: ' + entity['relevance']
				print 'sentiment: ' + entity['sentiment']['type']
				if 'score' in entity['sentiment']:
 					print 'score: ' + entity['sentiment']['score']
				print "\n"
		else:
			print('Error in entity extraction call: ', response['statusInfo'])


if __name__ == '__main__':
	main()
