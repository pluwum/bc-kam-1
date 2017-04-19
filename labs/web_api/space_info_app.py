from urllib.request import urlopen
from datetime import datetime
from urllib.error import URLError, HTTPError
import json

"""
This console application returns information from NASA with the help of Open Notify 
Open Notify is an open source project to provide a simple programming interface for some of NASA’s awesome data
"""


def getApiResponse(url):
	
	try:
		response = urlopen(url)
		if (response.getcode() == 200):
			response = response.read()
			jsonResponse = json.loads(response)
			return jsonResponse
		else:
			return {'message':'fail'}

	except URLError as e:
		print ('Accessing API resulted in a URL error code:', e)
		return {'message':'fail'}

	except HTTPError as e:
		print ('Accessing API resulted in an HTTP error code:', e.code)
		return {'message':'fail'}		

				
def getIssPosition():
	url = "http://api.open-notify.org/iss-now.json"
	response = getApiResponse(url)
	if(response['message'] == 'success'):
		position = response['iss_position']
		return "The ISS is at Latitude: {}, Longitude: {} right now".format(position['latitude'], position['longitude'])
	else:
		return "Ooops something went wrong, please try again later "	


def getIssDateAtPosition(latitude,longitude):
	if(abs(float(latitude)) <= 90 and abs(float(longitude)) <= 180):
		url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(latitude, longitude)
		response = getApiResponse(url)

		if(response['message'] == 'success'):
			response = response['response']
			passes = len(response)
			rises = []

			for rise in response:
				risetime = datetime.fromtimestamp(rise['risetime'])
				rises.append(str(risetime.strftime("* On %B %d, %Y at %H:%M:%S")))

			rises = "\n".join(rises)
			return "The ISS has {} upcoming passes at your specified location \n \n{}".format(passes,rises)

		else:
			return "Ooops something went wrong, please try again later "		
	else:
		return "One or more cordiantes entered is inavlid"		

def getNumberOfAstrosInSpaceNow():
	url = "http://api.open-notify.org/astros.json"
	response = getApiResponse(url)
	if(response['message'] == 'success'):
		count = response['number']
		response = response['people']
		astros = []

		for astro in response:
			astros.append("* Name: {} Craft: {}".format(astro['name'], astro['craft']))

		astros = "\n".join(astros)	
		return " There are {} astronuts in space right now\n \n{}".format(count,astros)

	else:
		return "Ooops something went wrong, please try again later "			


#Lets get input from Users

print("\n ########## Welcome to the NASA CLI information Center ########## \n")
print("Please specifiy the information you are looking for \n")
print(" 1: See the current location of the ISS \n")
print(" 2: Find out when the ISS will pass a location \n")
print(" 3: Know who is in space right now \n")
print(" 4: Quit \n")

option = input("Enter your choice here: ")


# Lets Proccess the inputs from the user
if(option == '1'):
	print (getIssPosition())

elif(option =='2'):
	latitude = input("Enter Latitude: ")
	longitude = input("Enter Longitude: ")
	
	print(getIssDateAtPosition(latitude,longitude))

elif(option == '3'):
	print(getNumberOfAstrosInSpaceNow())

elif(option == '4'):
	print("\n Good Bye")
else:
	print("Your input was invalid, please try again")