#!/usr/bin/python3
# getOpenWeather -- prints the weather for a location from the command line

APPID = '06e2c12f36297e6c963cf10666cf3760' #might be 'name' of api

import json, requests, sys

#compute location from command line arugments
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()
location = ' '.join(sys.argv[1:])
longitude = "36°9'14.33\" N"
latitude = "95°59'33.97\" W"
#TODO Download the json data from OpenweatherMap.org Api
url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={}&lon={}&appid={}'.format(latitude, longitude, APPID)
print(url)
response = requests.get(url)
response.raise_for_status()

print(response.text)
#TODO: Load json data ino a python variable 
