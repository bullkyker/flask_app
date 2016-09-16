# -*- coding: utf-8 -*-
# https://github.com/theskumar/python-dotenv
""" 
	Use geolocator and forcastio to get the weather
	for a given location.
	@author: Robert Quinn (bullkyker)
	@date:   9-2-2016
"""
import forecastio
from geopy.geocoders import Nominatim
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
geolocator = Nominatim()
import os

def get_weather(latitude, longitude, address):
	api_key = os.environ['FORECASTIO_API_KEY']
	lat = latitude
	lng = longitude
	api_key = api_key
	degree_sign = '\xb0'
	forecast = forecastio.load_forecast(api_key, lat, lng).currently()	
	return("{} and {}{} at {}".format(forecast.summary, forecast.temperature, degree_sign, address))
	
#Run it 

def get_location(my_location):	
	# prompt user for a location and convert to upper case
	# lower case states seems to break it.
	# for the sake of homework
	#your_location = input("Type in a valid address such as city, state: ").upper()
	your_location = my_location
	try:
		location = geolocator.geocode(your_location)
		latitude = location.latitude
		longitude = location.longitude
		address = location.address
	except AttributeError:
		print("You need to enter a valid address")		
		return
	#print(get_weather(latitude, longitude, address))
	current_weather = get_weather(latitude, longitude, address)
	return current_weather
# for the sake of homework assignment 
#get_location()

"""print(forecast.daily())
byHour = forecast.hourly()
print(byHour.summary)
print(byHour.icon)
for hourlyData in byHour.data:
	print(hourlyData.temperature)
"""