from urllib.request import urlopen
from datetime import datetime
import json

"""
This console application returns information from NASA with the help of Open Notify 
Open Notify is an open source project to provide a simple programming interface for some of NASA’s awesome data
"""


def getApiResponse(url):
	response = urlopen(url).read()
	jsonResponse = json.loads(response)
	return jsonResponse


def getIssPosition():
	url = "http://api.open-notify.org/iss-now.json"
	response = getApiResponse(url)
	position = response['iss_position']
	return "The ISS is at Latitude: {}, Longitude: {}".format(position['latitude'], position['longitude'])


def getIssDateAtPosition(latitude,longitude):
	url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(latitude, longitude)
	response = getApiResponse(url)
	response = response['response']
	passes = len(response)
	rises = []

	for rise in response:
		risetime = datetime.fromtimestamp(rise['risetime'])
		rises.append(str(risetime.strftime("* On %B %d, %Y at %H:%M:%S")))

	rises = "\n".join(rises)
	return "The ISS has {} upcoming passes at your specified location \n \n{}".format(passes,rises)


def getNumberOfAstrosInSpaceNow():
	url = "http://api.open-notify.org/astros.json"
	response = getApiResponse(url)
	count = response['number']
	response = response['people']
	astros = []

	for astro in response:
		astros.append("* Name: {} Craft: {}".format(astro['name'], astro['craft']))

	astros = "\n".join(astros)	
	return " There are {} astronuts in space right now\n \n{}".format(count,astros)


#print(getIssPosition())
#print(getIssDateAtPosition(40,-74))
#print(getNumberOfAstrosInSpaceNow())
#print( " The ISS is currently at latitude: {} , longitude: {}".format(iss_pos['latitude'],iss_pos['longitude']))

print("\n ########## Welcome to the NASA CLI information Center ########## \n")

print("Please specifiy the information you are looking for \n")
print(" 1: See the current location of the ISS \n")
print(" 2: Find out when the ISS will pass a location \n")
print(" 3: Know who is in space right now \n")
print(" 4: Quit \n")

option = input("Enter your choice here: ")

print(option)

if(option == '1'):
	getIssPosition()

elif(option =='2'):
	latitude = input("Enter Latitude: ")
	longitude = input("Enter Longitude: ")
	getIssDateAtPosition(longitude, latitude)

elif(option == '3'):
	getNumberOfAstrosInSpaceNow()

elif(option == '4'):
	print("\n Good Bye")
else:
	print("Your input was invalid, please try again")