import json
import requests
from random import choice
from time import sleep

accounts = [["replaceWithUserId", "replaceWithApiKey"],
	["replaceWithUserId2", "replaceWithApiKey2"]]

def getRandomString(length):
	"Returns a random string"
	chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	if 0 <= length <= 2000:
		return ''.join(choice(chars) for i in range(length))
	else:
		return ''.join(choice(chars) for i in range(10)) 
   
def getRandomUrl():
	"Returns a random URL"
	return "www.google.com/" + getRandomString(10);
	
def getRandomTag():
	"Returns a random tag"
	tag = '{"name": "' + getRandomString(60) +'", "id": "", "pack": { "name": "", "id": "", "color": 0 }, "url": ""}'
	return json.loads(tag)

def getRandomLink():
	"Returns a random link"
	link = '{ "id": "", "isPrivate": false, "thumbnailUrl": "", "thumbnailId": "", "tags": [{ "name": "' + \
	getRandomString(60) +'", "id": "", "pack": { "name": "", "id": "", "color": 0}, "url": "" }], "title": "' + \
	getRandomString(60) +'", "createdAt": "", "sourceUrl": "' + getRandomUrl() + \
	'", "thumbnailSource": "ThumbnailSource", "thumbnailSourceUrl": "", "url": "", "description": ""}'
	return json.loads(link)

def getRandomTagpack():
	"Returns a random tagpack"
	tagpack = '{ "name": "' + getRandomString(60) +'", "id": "", "color": 0}'
	return json.loads(tagpack)

def postTag(tagpackerConnection, headers):
	"Creates a new tag"
	try:
		response = requests.post(tagpackerConnection + '/tags', data=json.dumps(getRandomTag()), headers=headers)
		return response.json()
	except:
		print "Unexpected error:", sys.exc_info()[0]
	
def postTagpack(tagpackerConnection, headers):
	"Creates a new tagpack"
	try:
		response = requests.post(tagpackerConnection + '/tagpacks', data=json.dumps(getRandomTagpack()), headers=headers)
		return response.json()
	except:
		print "Unexpected error:", sys.exc_info()[0]
	
def postLink(tagpackerConnection, headers):
	"Creates a new link"
	try:
		response = requests.post(tagpackerConnection + '/links', data=json.dumps(getRandomLink()), headers=headers)
		return response.json()
	except:
		print "Unexpected error:", sys.exc_info()[0]

def post7Tags(tagpackerConnection, headers):
	"Creates 7 new tags"
	for i in range(7):
		print (postTag(tagpackerConnection, headers))
		
def post6Tagpacks(tagpackerConnection, headers):
	"Creates 6 new tagpacks"
	for i in range(6):
		print (postTagpack(tagpackerConnection, headers))
		
def post7Links(tagpackerConnection, headers):
	"Creates 7 new links"
	for i in range(7):
		print (postLink(tagpackerConnection, headers))
	
def runSpammer():
	"Spams tagpacker's API"
	for i in range(len(accounts)):
		headers = {'content-type': 'application/json', 'api_key': accounts[i][1]}
		tagpackerConnection = "https://tagpacker.com/api/users/" + accounts[i][0]
		# 20 requests per minute per user/ api key
		post7Tags(tagpackerConnection, headers)
		post6Tagpacks(tagpackerConnection, headers)
		post7Links(tagpackerConnection, headers)
	
runSpammer()
print ("Done")