#! /user/bin/python
#! -*- coding: utf-8 -*-
import sys
import urllib, urllib2
import json

"""
Reversion HeyooDic
Transfer from unoffical API to offical API

Chrisplus
2014-6
"""

# Key and name
url = "http://fanyi.youdao.com/openapi.do?%s"
keyFrom = "SunnyArtStudio"
key = "1884243682"
dataType = "data"
docType = "json"
version = "1.1"
queryWord = ""
# dic or translate
only = "" 

def main(argv):
	if len(argv) == 1:
		queryword = argv[0]
		sendRequest(queryword, None)
	elif len(argv) == 2:
		if argv[0] == "-d":
			only = "dict"
			queryword = argv[1]
			sendRequest(queryword, only)
		elif argv[0] == "-t":
			only = "tanslate"
			queryword = argv[1]
			sendRequest(queryword, only)
		else:
			printUsage()
	else:
		printUsage()


def printUsage():
	print "Dic.py -d or -t word" 

def sendRequest(keyword, selection):
	# build parameters
	if keyword is None or not keyword:
		return -1

	param = {}
	param.update({'keyfrom' : keyFrom})
	param.update({'key' : key})
	param.update({'type': dataType})
	param.update({'doctype': docType})
	param.update({'version': version})

	if selection is not None:
		param.update({'only': selection})

	param.update({'q': keyword})

	# build url and send request
	requestUrl = url % urllib.urlencode(param)
	content = urllib2.urlopen(requestUrl).read()
	parseContent(content)

def parseContent(content):
	try:
		jsonData = json.loads(content)
	except ValueError:
		print "Invalid Json Content"
		return -1

	# handle error code
	errorCode = jsonData['errorCode']
	if errorCode == 0:
		# successful
		showResult(jsonData)
	elif errorCode == 20:
		print "Too many words"
	elif errorCode == 30:
		print "I cannot do it"
	elif errorCode == 40:
		print "I have no idea"
	elif errorCode == 50:
		print "Invalid key"
	elif errorCode == 60:
		print "No results"

	#finish

def showResult(jsondata):
	#First


if __name__ == "__main__":
	main(sys.argv[1:])