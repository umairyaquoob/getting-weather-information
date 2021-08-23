import requests
from pprint import pprint

API_Key = '684ad6f971fd10de0223a6fab47ddb30'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
