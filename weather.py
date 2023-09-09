import requests
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
OWM_API_KEY = os.environ['OWM_API_KEY']

weather_params = {
    "lat": os.environ['MY_HOME_LATITUDE'],
    "lon": os.environ['MY_HOME_LONGITUDE'],
    "appid": OWM_API_KEY,
    "units": "imperial",
    "exclude": "current,minutely,hourly"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()['daily'][0]

low_temp = round(float(data['temp']['min']))
high_temp = round(float(data['temp']['max']))
pop = round(float(data['pop']) * 100)
description = data['weather'][0]['description']
icon = data['weather'][0]['icon']
