#!/usr/bin/python
__author__ = 'jshirley'
import requests
import argparse
import json

URL_TEMPLATE = "http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&units=metric&cnt=7"

parser = argparse.ArgumentParser(description='Get location code')
parser.add_argument('-l', help='location code to display results for', required=True)

args = parser.parse_args()
loc_code = args.l

url = URL_TEMPLATE.format(loc_code)

response = requests.get(url)
responseObj = json.loads(response.text)
if responseObj['cod'] != 200:
    raise ValueError

city = responseObj['city']

city_name = city['name']
country = city['country']

city_coords = city['coord']
latitude = city_coords['lat']
longitude = city_coords['lon']

print(city_name + ', ' + country + ' - ' + 'lat: ' + latitude + ', ' + 'lon: ' + longitude)

forecastList = responseObj['list']